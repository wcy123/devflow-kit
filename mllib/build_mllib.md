
# setup Vitis development environment.

```
% ssh -J  localhost:10022 xcdl190344.xilinx.com
% ls -l /proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/
% source /opt/xilinx/xrt/setup.sh
% source /proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/settings64.sh
% cd /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression;ls -l
```


# debug x86sim

```
% python3 -m pip install --user torch numpy # not ~/.config/pip/config , cert file is different for Ubuntu and CentOS.
% # check https://confluence.xilinx.com/display/~fuweiy/Copy+of+How+to+install+python%2C+pip%2C+pypi+packages+in+XCD for more details.
% ls $XILINX_VITIS/gnu/aarch64/lin/aarch64-linux/aarch64-xilinx-linux
% cd /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/conv/Conv2D_0;ls -l
% make -n x86sim DEBUG=yes TARGET=x86sim PYTHON_PATH=`which python3` DEVICE="xilinx_vck190_base_202310_1" PLATFORM_REPO_PATHS=$XILINX_VITIS/base_platforms SYSROOT=$XILINX_VITIS/gnu/aarch64/lin/aarch64-linux/aarch64-xilinx-linux

```

error

```
% sim.out: /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/aietools/include/aie_api/aie.hpp:765: vector<aie_dm_resource_remove_t<T>, Elems> aie::load_v(const T *) [Elems = 32, Resource = aie_dm_resource::none, T = unsigned char]: Assertion `detail::check_vector_alignment<Elems>(ptr) && "Insufficient alignment"' failed.
```

see https://confluence.xilinx.com/display/XSW/Simulating+AIE-ML+designs+with+x86sim


```
% cd /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/conv/Conv2D_8;ls -l
% aiecompiler  --target=x86sim --pl-freq= --log-level=1  --aiearch=aie-ml --disable-multirate-analysis --enable-multi-layer --include=/proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/aietools/include/aie_api -I /proj/xbuilds/SWIP_plus/9999.0_0401_2052plus/installs/lin64/Vitis/2023.2/aietools/include -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/include/conv/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/include/common/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/src/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/inc/ /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/src/test_conv2d.cpp
% x86simulator --pkg-dir=./Work --input-dir=./ --output-dir=./ --gdb
% b conv2d.h:510
% b conv2d_params.h:601
% p inc_Xi
% p inc_Kx
% p num_Kx
% p inc_Ky
% p num_Ky
% p inc_Ci
% p param
% c
% p conv2d_params
% p conv2d_params.outer_g
% p conv2d_params.conv_type
% r
% y
% p fc_mode
% n
% p param.ifm_xsize
% p param.ifm_ysize
% p param.ifm
% p param.num_ofm_ch
% p param.num_ofm_ch
% p param.oxp
% p param.oyp
% p param.kx
% p param.ky
% p param.outer_g
outer_g = X_g  * param.oyp  * Co_g;
10      = 1    * 5 * 2

% p Co_g
Co_g=2 ofms = 16, ofms/8
o
% p param.inner_g
=4 param.kx * param.ky * Ci_g;
=  1 * 1 * 4
% p sv_out_width
=16 param.oxp + ((calc_edge_output<<4)>>param.batch_log2)
% p calc_edge_output
% p param.outer_g
% p fc_mode
% p X_g
X_g = sv_out_width * batch / 16
= 2
% p sv_out_width
= 8
% p param.batch
= 4,
% p param.num_X
=0
% p param.num_Co
=1
% p ixp
ixp = 16
% p iyp
iyp = 5
% p nofms # 32
% p param.num_ofm_ch
= 32
% p param.ifm
= 32
% p Ci_g
Ci_g = 4 = ifms/8, ifms = 32.
% outer_g
% p chnd_T
% b conv2d.h:535
% n
% p p_in
% p conv2d_params.inc_A
% conv2d_params.iterator_inner_incr2
```

```
# conv0
$12 = (conv2d_params_t &) @0x4a9640: {
  ifm_xsize = 16 '\020', ifm_ysize = 5 '\005', ifm = 32 ' ', num_ofm_ch = 32 ' ',
  ksize = 1 '\001', stride_bits = 0 '\000', shift_out = 8 '\b', out_mode = 0 '\000',
  shift_bias_init = 0 '\000', shift_psum_in = 0 '\000', shift_psum_out = 0 '\000', psum_buff_offset_scaled = 1 '\001',
  lrelu_alpha = 0, shift_lrelu_alpha = 15 '\017', shift_lrelu_input = 0 '\000',
  shift_lrelu_out = 7 '\a', num_chout_iter = 1 '\001', num_ifm_depth_iter = 8 '\b', op_mode = 0 '\000',
  ofm_len = 2560, num_height_iter = 1 '\001', num_width_iter = 1 '\001',
  ifm_len = 2560, ofm_width_pad = 0 '\000', run_time_act = 0 '\000',
  conv_type = 0 '\000', row_offset = 0 '\000', in0_sign = 0 '\000', ifm_sign = 1,
  ofm_offset_packed = 0 '\000', out_sign = 1, psum_buff_offset = 128, ofm_offset_left = 0 '\000', psum_in = 0, psum_out = 1, hdr_len = 80, batch = 1 '\001', batch_log2 = 0 '\000', oyp = 5 '\005',
  oxp = 16 '\020', ky = 1 '\001', kx = 1 '\001', stride = 1 '\001', curr_depth_iter = 1 '\001', io_mode = 1 '\001', ofm_offset_top = 0, exec_type = 1 '\001', inner_g = 4, outer_g = 10, ifm_offset = 0, wts_offset = 0,
  iterator_inner_incr0 = -88, iterator_inner_incr1 = 416, iterator_inner_wrap0 = 0, iterator_inner_wrap1 = 0, iterator_inner_incr2 = 32, iterator_outer_incr0 = -384, iterator_outer_incr1 = -512, iterator_outer_wrap0 = 0,
  iterator_outer_wrap1 = 1, iterator_outer_incr2 = 0, iterator_weights_incr0 = -512, iterator_weights_incr1 = 0, iterator_weights_wrap0 = 0, iterator_weights_wrap1 = 1, iterator_weights_incr2 = -1024, inc_A = 32, inc_A_1 = 0, inc_Co = 64,
  inc_Xo = -64, inc_Co_T = 128, inc_Xo_T = -128, inc_S_0 = 64, inc_S_1 = 64, inc_S_2 = 0, inc_ST_0 = 128, inc_ST_1 = 128, inc_ST_2 = 0, inc_acc_0 = 0, inc_acc_1 = 64, inc_acc_2 = -64, inc_acc_d0 = 0, inc_acc_d1 = 128, inc_acc_rev = -128,
# conv8
$40 = (conv2d_params_t &) @0x4a6620: {
  ifm_xsize = 8 '\b', ifm_ysize = 5 '\005', ifm = 32 ' ', num_ofm_ch = 32 ' ', ksize = 1 '\001', stride_bits = 0 '\000',
  shift_out = 8 '\b', out_mode = 0 '\000', shift_bias_init = 0 '\000', shift_psum_in = 0 '\000', shift_psum_out = 0 '\000', psum_buff_offset_scaled = 2 '\002',
  lrelu_alpha = 0, shift_lrelu_alpha = 15 '\017', shift_lrelu_input = 0 '\000', shift_lrelu_out = 7 '\a', num_chout_iter = 1 '\001', num_ifm_depth_iter = 1 '\001',
  op_mode = 0 '\000', ofm_len = 5120, num_height_iter = 1 '\001', num_width_iter = 1 '\001', ifm_len = 5120, ofm_width_pad = 0 '\000', run_time_act = 0 '\000',
  conv_type = 0 '\000', row_offset = 0 '\000', in0_sign = 0 '\000', ifm_sign = 1, ofm_offset_packed = 0 '\000', out_sign = 1, psum_buff_offset = 256,
  ofm_offset_left = 0 '\000', psum_in = 0, psum_out = 0, hdr_len = 80, batch = 4 '\004', batch_log2 = 2 '\002', oyp = 5 '\005', oxp = 8 '\b', ky = 1 '\001', kx = 1 '\001',
  stride = 1 '\001', curr_depth_iter = 0 '\000', io_mode = 0 '\000', ofm_offset_top = 0, exec_type = 0 '\000', inner_g = 4, outer_g = 20, ifm_offset = 0, wts_offset = 0,
  iterator_inner_incr0 = -64, iterator_inner_incr1 = 928, iterator_inner_wrap0 = 0, iterator_inner_wrap1 = 0, iterator_inner_incr2 = 160, iterator_outer_incr0 = -896,
  iterator_outer_incr1 = -1152, iterator_outer_wrap0 = 1, iterator_outer_wrap1 = 1, iterator_outer_incr2 = -128, iterator_weights_incr0 = -512, iterator_weights_incr1 = 0,
  iterator_weights_wrap0 = 1, iterator_weights_wrap1 = 1, iterator_weights_incr2 = -1024, inc_A = 32, inc_A_1 = 0, inc_Co = 64, inc_Xo = -192, inc_Co_T = 128,
  inc_Xo_T = -384, inc_S_0 = 64, inc_S_1 = 192, inc_S_2 = 0, inc_ST_0 = 128, inc_ST_1 = 384, inc_ST_2 = 0, inc_acc_0 = 0, inc_acc_1 = 64, inc_acc_2 = -64, inc_acc_d0 = 0,
  inc_acc_d1 = 128, inc_acc_rev = -128, step_align = 0, shfl_0 = 22, shfl_1 = 23, shfl_2 = 0, num_Kx = 0 '\000', num_Co = 1, num_X = 1, num_W = 0 '\000', num_BN = 0 '\000'}

inc_Kx = -64
inc_Ky = 928
num_Kx = 0
num_Ky = 0
inc_Ci = 160
inc_Co_rev = -1152
inc_Xi = -896
inc_Yi = -128
inc_w_Ci_rev = -512
inc_w_Co_rev = -1024
calc_edge_output = 0
tmp = 16 '\020'
nofms = 32 ' '
ksize = 1 '\001'
stride_bits = 0 '\000'
nifms = 32 ' '
fc_mode = 0
value = 0
ksize_x = 1 '\001'
ksize_y = 1 '\001'
stride_bits_x = 0 '\000'
--Type <RET> for more, q to quit, c to continue without paging--p paramc
stride_bits_y = 0 '\000'
stride_x = 1 '\001'
stride_y = 1 '\001'
sv_out_width = 8
align_kx = 1
ixp = 8
iyp = 5
step_co = 256
step_ci = 256
step_yo = 1024
step_yi = 1024
N_g = 4 '\004'
X_g = 2 '\002'
Co_g = 2 '\002'
num_Kx_adj = 0 '\000'
Ci_g = 4 '\004'
step_Xo = 8
step_Yi = 1024
step_Xi = 8
step_Ky = 1024
step_Kx = 32
SN0_g = 1
SN1_g = 4
chnd = 32
chnd_T = 64
bits_O = 8
bits_T = 16
inc_S_0_base = 64
inc_ST_0_base = 128
$17 = (conv2d_params_t &) @0x4a6620: {
  ifm_xsize = 8 '\b',
  ifm_ysize = 5 '\005',
  ifm = 32 ' ',
  num_ofm_ch = 32 ' ',
  ksize = 1 '\001',
  stride_bits = 0 '\000',
  shift_out = 8 '\b',
  out_mode = 0 '\000',
  shift_bias_init = 0 '\000',
  shift_psum_in = 0 '\000',
  shift_psum_out = 0 '\000',
  psum_buff_offset_scaled = 2 '\002',
  lrelu_alpha = 0,
  shift_lrelu_alpha = 15 '\017',
  shift_lrelu_input = 0 '\000',
  shift_lrelu_out = 7 '\a',
  num_chout_iter = 1 '\001',
  num_ifm_depth_iter = 1 '\001',
  op_mode = 0 '\000',
  ofm_len = 5120,
  num_height_iter = 1 '\001',
  num_width_iter = 1 '\001',
  ifm_len = 5120,
  ofm_width_pad = 0 '\000',
  run_time_act = 0 '\000',
  conv_type = 0 '\000',
  row_offset = 0 '\000',
  in0_sign = 0 '\000',
  ifm_sign = 1,
===============>
  ofm_offset_packed = 0 '\000',
  out_sign = 1,
  psum_buff_offset = 256,
  ofm_offset_left = 0 '\000',
  psum_in = 0,
  psum_out = 0,
  hdr_len = 80,
  batch = 4 '\004',
  batch_log2 = 2 '\002',
  oyp = 5 '\005',
  oxp = 8 '\b',
  ky = 1 '\001',
  kx = 1 '\001',
    stride = 1 '\001',
  curr_depth_iter = 0 '\000',
  io_mode = 0 '\000',
  ofm_offset_top = 0,
  exec_type = 0 '\000',
  inner_g = 4,
  outer_g = 20,
  ifm_offset = 0,
  wts_offset = 0,
  iterator_inner_incr0 = -64,
  iterator_inner_incr1 = 928,
  iterator_inner_wrap0 = 0,
  iterator_inner_wrap1 = 0,
  iterator_inner_incr2 = 160,
  iterator_outer_incr0 = -896,
  iterator_outer_incr1 = -1152,
  iterator_outer_wrap0 = 1,
  iterator_outer_wrap1 = 1,
  iterator_outer_incr2 = -128,
  iterator_weights_incr0 = 0,
  iterator_weights_incr1 = 0,
  iterator_weights_wrap0 = 0,
  iterator_weights_wrap1 = 0,
  iterator_weights_incr2 = 0,
  inc_A = 32,
  inc_A_1 = 0,
  inc_Co = 64,
  inc_Xo = -192,
  inc_Co_T = 128,
  inc_Xo_T = -384,
  inc_S_0 = 64,
  inc_S_1 = 192,
  inc_S_2 = 0,
  inc_ST_0 = 128,
  inc_ST_1 = 384,
  inc_ST_2 = 0,
  inc_acc_0 = 0,
  inc_acc_1 = 64,
  inc_acc_2 = -64,
  inc_acc_d0 = 0,
  inc_acc_d1 = 128,
  inc_acc_rev = -128,
  step_align = 0,
  shfl_0 = 22,
  shfl_1 = 23,
  shfl_2 = 0,
  num_Kx = 0 '\000',
  num_Co = 1,
  num_X = 1,
  num_W = 0 '\000',
  num_BN = 0 '\000'
(gdb)
```


```
template <unsigned M, unsigned K, unsigned N, typename TypeA, typename TypeB, unsigned AccumBits>
struct mmul;
Cbuff0 aie::mmul<4, 8, 8, signed char, signed char, accauto>
Cbuff3.mac(vec_Xbuff3, Ybuff0);

vector<i8, 32> vec_Xbuff3
vector<i8, 64> vec_Ybuff0
  4x8 * 8x8
= 4x8


test case

ifm = 1x5x16x256
ofm = 1x5x16x32
k=32x1x1x256

weight header vector<int,8>
16 5 32 32
ifm_xsize = 16
ifm_ysize = 5
ifm = 32
num_ofm_ch = 32

1 0 8 0
ksize = 1
stride_bits = 0
shift_out = 8
out_mode = 0
0 0 0 1
shift_bias_init = 0
shift_psum_in = 0
shift_psum_out = 0
psum_buff_offset_scaled = 1
0 0 15 0
lrelu_alpha = 0,
relu_alpha = 0
shift_lrelu_alpha = 15
shift_lrelu_input = 0
7 1 8 0
shift_lrelu_out = 7
num_chout_iter = 1
num_ifm_depth_iter = 8
op_mode = 0
0 10 1 1
ofm_len = 2560
num_height_iter = 1
num_width_iter = 1
0 10 0 0
ifm_len = 2560
ofm_width_pad = 0
run_time_act = 0
0 0 16 0
conv_type = 0 '\000'
row_offset = 0
in0_sign = 0
ifm_sign = 1

```

```
% Ci_g = ifm / 8
% param.inner_g               = param.kx * param.ky * Ci_g;
%
```

# backup


```
% vi /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/aietools/include/aie_api/aie.hpp
%
% make all DEBUG=yes TARGET=x86sim PYTHON_PATH=`which python3` DEVICE="xilinx_vck190_base_202310_1" PLATFORM_REPO_PATHS=$XILINX_VITIS/base_platforms SYSROOT=$XILINX_VITIS/gnu/aarch64/lin/aarch64-linux/aarch64-xilinx-linux
```

## cannot find `xaiengine.h` no need to fix it.

# backup
```
xcdl190268:/group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/conv/Conv2D_0% make all PYTHON_PATH=/wrk/xcdhdnobkup1/chunywan/opt/bin/python3 LD_LIBRARY_PATH="/wrk/xcdhdnobkup1/chunywan/opt/lib" DEVICE="xilinx_vck190_base_202310_1" PLATFORM_REPO_PATHS=/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/nt64/Vitis/2023.2/base_platforms SYSROOT=/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux

```

```
path    (/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis_HLS/2023.2/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Model_Composer/2023.2/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/microblaze/lin/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/arm/lin/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch32/lin/gcc-arm-none-eabi/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch64/lin/aarch64-none/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/armr5/lin/gcc-arm-none-eabi/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/tps/lnx64/cmake-3.3.2/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/aietools/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vivado/2023.2/bin /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/DocNav /proj/xbuilds/HEAD_plus_daily_latest/installs/lin64/Vitis/HEAD/aietools/bin /home/chunywan/.cargo/bin /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin /usr/games /usr/local/games /snap/bin /opt/puppetlabs/bin)
```



edit make file aie/Makefile

```
0_0_orig.cpp:
    ${XCHESSCC} +f +s -p me -P ${CARDANO_AIE_ARCH_MODEL_DIR} +P 4  +Wllvm,-O2,-fno-jump-tables,-fno-discard-value-names,-mllvm,-chess-collapse-struct-types-during-linking=0,-Xclang,-chess-only-info-critical-passes,-g -D__AIENGINE__ -D__AIEARCH__=20 -D__LOCK_FENCE_MODE__=0 -DAIE_OPTION_SCALAR_FLOAT_ON_VECTOR -DAIE2_\
FP32_EMULATION_ACCURACY_FAST ${INCLUDE_PATH} -E /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/conv/Conv2D_0/Work/aie/0_0/src/0_0.cc -o ir/0_0_orig.cpp;
```


see

```



make all HOST_ARCH=x86 DEBUG=yes TARGET=x86sim PYTHON_PATH=/wrk/xcdhdnobkup1/chunywan/opt/bin/python3 LD_LIBRARY_PATH="/wrk/xcdhdnobkup1/chunywan/opt/lib" DEVICE="xilinx_vck190_base_202310_1" PLATFORM_REPO_PATHS=/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/nt64/Vitis/2023.2/base_platforms SYSROOT=/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux SYSROOT=/proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux/x86_64-petalinux-linux
```

```
% g++ -std=c++11 -I /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/aietools/include/aie_api -I /proj/xbuilds/SWIP_plus/9999.0_0321_0854plus/installs/lin64/Vitis/2023.2/aietools/include -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/include/conv/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/include/common/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/src/ -I /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/inc/ -E -o ./a.txt -I. /group/dphi_software/software/workspace/chunywan/d/working/xdock-vitis-ai-sw/workspace/mllib/L1/regression/src/conv2d_wrapper.cpp
``

```
conv 0.
:Conv_DPU_0 chunywan % cat data/ifms.txt  |  wc
   5120   20480   74657
ifm 5120 * 4 = 20480
:Conv_DPU_0 chunywan % cat data/weights.txt  |  wc
   2688    9728   33225

weight size = (* 2668 4) = 10672

ifm (* 1 5 16 256) = 20480 IN_SIZE, Cin = 256
ofm (* 1 5 16 32) = 2560 = OUT_SIZE_BYTES, Cin = 256
Kernel = 32x1x1x256   (* 32 1 1 256) = 8192
(+ 2560 (* 4 2560) 2560)
sub volume
Kernel = 32x1x1x256   (* 32 1 1 32) = 1024
(+ 1024 320) = 1344
80 * 4

int * weights = (int*) wts.data() + conv2d_params.hdr_len + conv2d_params.wts_offset ;

conv2d_params.hdr_len = 80
(* 4 80) =  320
(+ 1024 320) = 1344
(_sizes = {1344})
(gdb) p sizeof(layer_params) = 280

(+ (* 1024 8) 320) = 17052


stride = 1

ifm sub volume (* 1 5 16 32)
num of iter = (/ 256 32) = 8



NUM_DEPTH_ITERS = 8
```


(gdb) p output
$50 = (int *) 0x215c5a0
