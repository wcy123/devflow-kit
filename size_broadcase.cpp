#include <cstdlib>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
#define UNI_LOG_FATAL(x) std::cout

// https://numpy.org/doc/stable/user/basics.broadcasting.html
// General Broadcasting Rules
// When operating on two arrays, NumPy compares their shapes element-wise. It
// starts with the trailing (i.e. rightmost) dimensions and works its way left.
// Two dimensions are compatible when

// they are equal, or

// one of them is 1

// If these conditions are not met, a ValueError: operands could not be
// broadcast together exception is thrown, indicating that the arrays have
// incompatible shapes. The size of the resulting array is the size that is not
// 1 along each axis of the inputs.

// Arrays do not need to have the same number of dimensions. For example, if you
// have a 256x256x3 array of RGB values, and you want to scale each color in the
// image by a different value, you can multiply the image by a one-dimensional
// array with 3 values. Lining up the sizes of the trailing axes of these arrays
// according to the broadcast rules, shows that they are compatible:

// Image  (3d array): 256 x 256 x 3
// Scale  (1d array):             3
// Result (3d array): 256 x 256 x 3
// When either of the dimensions compared is one, the other is used. In other
// words, dimensions with size 1 are stretched or “copied” to match the other.

// In the following example, both the A and B arrays have axes with length one
// that are expanded to a larger size during the broadcast operation:

// A      (4d array):  8 x 1 x 6 x 1
// B      (3d array):      7 x 1 x 5
// Result (4d array):  8 x 7 x 6 x 5
// Here are some more examples:

// A      (2d array):  5 x 4
// B      (1d array):      1
// Result (2d array):  5 x 4

// A      (2d array):  5 x 4
// B      (1d array):      4
// Result (2d array):  5 x 4

// A      (3d array):  15 x 3 x 5
// B      (3d array):  15 x 1 x 5
// Result (3d array):  15 x 3 x 5

// A      (3d array):  15 x 3 x 5
// B      (2d array):       3 x 5
// Result (3d array):  15 x 3 x 5

// A      (3d array):  15 x 3 x 5
// B      (2d array):       3 x 1
// Result (3d array):  15 x 3 x 5
// Here are examples of shapes that do not broadcast:

// A      (1d array):  3
// B      (1d array):  4 # trailing dimensions do not match

// A      (2d array):      2 x 1
// B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
// An example of broadcasting in practice:

// >>> x = np.arange(4)
// >>> xx = x.reshape(4,1)
// >>> y = np.ones(5)
// >>> z = np.ones((3,4))

// >>> x.shape
// (4,)

// >>> y.shape
// (5,)

// >>> x + y
// ValueError: operands could not be broadcast together with shapes (4,) (5,)

// >>> xx.shape
// (4, 1)

// >>> y.shape
// (5,)

// >>> (xx + y).shape
// (4, 5)

// >>> xx + y
// array([[ 1.,  1.,  1.,  1.,  1.],
//        [ 2.,  2.,  2.,  2.,  2.],
//        [ 3.,  3.,  3.,  3.,  3.],
//        [ 4.,  4.,  4.,  4.,  4.]])

// >>> x.shape
// (4,)

// >>> z.shape
// (3, 4)

// >>> (x + z).shape
// (3, 4)

// >>> x + z
// array([[ 1.,  2.,  3.,  4.],
//        [ 1.,  2.,  3.,  4.],
//        [ 1.,  2.,  3.,  4.]])
// Broadcasting provides a convenient way of taking the outer product (or any
// other outer operation) of two arrays. The following example shows an outer
// addition operation of two 1-d arrays:

// >>> a = np.array([0.0, 10.0, 20.0, 30.0])
// >>> b = np.array([1.0, 2.0, 3.0])
// >>> a[:, np.newaxis] + b
// array([[  1.,   2.,   3.],
//        [ 11.,  12.,  13.],
//        [ 21.,  22.,  23.],
//        [ 31.,  32.,  33.]])
// Here the newaxis index operator inserts a new axis into a, making it a
// two-dimensional 4x1 array. Combining the 4x1 array with b, which has shape
// (3,), yields a 4x3 array

std::tuple<bool, std::vector<std::int32_t>> size_broadcast(
    const std::vector<std::int32_t>& in_a,
    const std::vector<std::int32_t>& in_b) {
  // new imp
  bool if_success = false;
  std::vector<std::int32_t> ret;
  std::vector<std::int32_t> in_a_local, in_b_local;
  // here make the in_a_local is longer than in_b_local
  if (in_a.size() > in_b.size()) {
    in_a_local = in_a;
    in_b_local = in_b;
  } else {
    in_a_local = in_b;
    in_b_local = in_a;
  }
  auto size_a = in_a_local.size();
  auto size_b = in_b_local.size();
  ret.resize(size_a);
  if (in_a_local == in_b_local) {
    if_success = true;
    ret = in_a_local;
  } else if ((size_a == 0) || (size_b == 0)) {
    if_success = true;
    if (size_a == 0) {
      ret = in_b;
    } else if (size_b == 0) {
      ret = in_a;
    }
  } else {
    std::int32_t idx_a = size_a - 1;
    std::int32_t idx_b = size_b - 1;
    std::int32_t idx_ret = size_a - 1;
    for (; idx_ret >= 0; idx_ret--) {
      if ((idx_a >= 0) && (idx_b >= 0)) {
        auto dim_a = in_a_local[idx_a];
        auto dim_b = in_b_local[idx_b];
        if (dim_a == 1) {
          ret[idx_ret] = dim_b;
          idx_a--;
          idx_b--;
        } else if (dim_b == 1) {
          ret[idx_ret] = dim_a;
          idx_a--;
          idx_b--;
        } else if (dim_a == dim_b) {
          ret[idx_ret] = dim_a;
          idx_a--;
          idx_b--;
        } else {
          break;
        }
      } else if ((idx_a >= 0) && (idx_b < 0)) {
        auto dim_a = in_a_local[idx_a];
        ret[idx_ret] = dim_a;
        idx_a--;
      } else if ((idx_a < 0) && (idx_b >= 0)) {
        break;
      } else {
        abort();
      }
    }
    if_success = (idx_ret < 0);
  }
  return std::make_tuple(if_success, ret);
}

ostream& operator<<(ostream& s, const std::vector<int>& v) {
  s << "[";
  for (auto c = 0u; c < v.size(); ++c) {
    if (c != 0) {
      s << ",";
    }
    s << v[c];
  }
  s << "]";
  return s;
}

int main(int argc, char* argv[]) {
  // vector<int> a = {8, 1, 6, 1};
  // vector<int> b = {7, 1, 5};
  // vector<int> a = {5, 4};
  // vector<int> b = {1};
  // vector<int> a = {15, 3, 5};
  // vector<int> b = {3, 5};
  // vector<int> a = {15, 3, 2};
  // vector<int> b = {3, 5};
  vector<int> a = {15, 3, 2};
  vector<int> b = {};
  vector<int> c;
  bool ok;
  tie(ok, c) = size_broadcast(a, b);
  cout << "ok = " << ok << " " << c << endl;
  return 0;
}
