# Introduction about graph runner.

## Overview

It takes the following steps to deploy a model of TF, PyTorch or Caffe on an FPGA/AIE platform.

1. Quantize the model, i.e. convert float format into int8 format.
2. Compile the quantized model into a XIR graph, a universal representation of the model as a computational graph.
3. Invoke VART APIs to run the XIR graph

This artical focuses on the step 3 and assume we already have a XIR
graph in handle. For other two steps, please refer to (TODO: links to
other resources).

## Quick introduction about XIR graph

An XIR graph is a simple representation of a computational DAG
(Directed Acyclic Graph) whereas nodes are operations, i.e. `XIR Op`
e.g.  conv2d, reshape, concatenation etc. An `XIR Op` has only one
`XIR Tensor` as output and one or many `XIR Tensor` as inputs. The
`Xcompiler` (TODO: refer to step 2) marks some `XIR Ops` as inputs and
some `XIR Ops` as outputs.

An XIR graph is segmented into many subgraphs, and each subgraph has
corresponding runner to run the subgraph on a specific device,
e.g. "DPU", "CPU" or others. Without graph runner APIs, the end user
have to create these runners and manually connect inputs and outputs
between the runners. This process is error-prone. With graph runner APIs, the
end user only need to take care of the inputs and outputs of the
whole graph.

For ease of use, we dedicately design the graph runner APIs as same as
subgraph runner APIs. They share the same API interface,
i.e. `vart::Runner` or `vart::RunnerExt` which is an extension of
`vart::Runner`.


## An example

Let's take `resnet50.xmodel` as an exmaple to show how to deploy the
model on a target board. Basically it includes the following steps:

1. load the xmodel file.
2. create a graph runner.
3. fill in inputs
4. start the runner
5. post process the output.


To load a xmodel file, we can use XIR API `xir::Graph::deserialize`. (TODO: refer to XIR links)

``` c++
auto g_xmodel_file = std::string("/usr/share/vitis_ai_library/models/resnet50/resnet50.xmodel")
auto graph = xir::Graph::deserialize(g_xmodel_file);
```

To create a runner, we can use one of Vitis-AI-Library API,
`vitis::ai::GraphRunner::create_graph_runner` (TODO refer to Vitis-AI-

``` c++
auto attrs = xir::Attrs::create();
auto runner =
      vitis::ai::GraphRunner::create_graph_runner(graph.get(), attrs.get());
```

`attrs` is not in use yet.

To fill in inputs, we need to use VART API,
`vart::RunnerExt::get_inputs()` , (TODO: refer to VART link), it
returns the input tensor buffers associated with the output `XIR Ops`
marked by `Xcompiler` as mentioned above.

``` c++
std::vector<vart::TensorBuffer*> inputs = runner->get_inputs();
```

For `resnet50.xmodel`, we have only one input tensor buffers.

```
auto tensor_buffer= inputs[0];
auto batch_size = inputs[0]->get_tensor()->get_shape()[0];
uint64_t data;
size_t data;
for(auto batch = 0; batch < batch_size; ++ batch) {
    std::tie(data, size) = tensor_buffer->data({batch, 0, 0, 0});
    // read input from file
    ...
}
```

A input tensor buffer has many continuous memory regions, and one
region for one input image in the batch so that we have to read image
and fill in input one by one.

If the number of input images is less than the batch size, we have to
construct a new tensor buffer that has a smaller batch size. It is not
recommended because DPU resource is not fully utilized.

We can read data from a input file as below.

``` c++
std::ifstream(filename).read((char*)data, size).good()
```

We can start the graph runner as below.

``` c++
  //sync input tensor buffers
  for (auto& input : inputs) {
      input->sync_for_write(0, input->get_tensor()->get_data_size() /
                                   input->get_tensor()->get_shape()[0]);
  }

  //run graph runner
  auto v = runner->execute_async(inputs, outputs);
  auto status = runner->wait((int)v.first, -1);
  CHECK_EQ(status, 0) << "failed to run the graph";

  //sync output tensor buffers
  for (auto output : outputs) {
      output->sync_for_read(0, output->get_tensor()->get_data_size() /
                                   output->get_tensor()->get_shape()[0]);
  }

```

It is important to synchronize buffers i.e. before and after
`execute_async` because potentially it is possible to support
preprocessing and postprocessing by HW with zero-copy so that
synchronization becomes necessary in such case.


Similar to fill in input tensor buffers, we can read and process the
output tensor buffers as below.

``` c++
auto tensor_buffer= outputs[0];
auto batch_size = outputs[0]->get_tensor()->get_shape()[0];
uint64_t data;
size_t data;
for(auto batch = 0; batch < batch_size; ++ batch) {
    std::tie(data, size) = tensor_buffer->data({batch, 0, 0, 0});
    std::ofstream(filename).write((char*)data, size).good();
}
```

Note that output tensor buffers are not ordered, we need to be careful
to find the proper output tensor buffers by name, i.e.
`tensor_buffer->get_tensor()->get_name()`
