#include <dlfcn.h>

#include <iostream>
using namespace std;
typedef const char* (*fun)();
fun load(const char* name) {
  auto so_name = name;
  auto handle = dlopen(so_name, RTLD_LAZY | RTLD_GLOBAL);
  if (!handle) {
    cerr << "cannot open plugin: name=" << so_name;
    abort();
  };
  auto ret = (fun)dlsym(handle, "hello");
  if (ret == nullptr) {
    cerr << "not a valid plugin, cannot find symbol " << so_name;
  }
  return ret;
}

int main(int argc, char* argv[]) {
  auto foo = load(argv[1]);
  auto bar = load(argv[2]);
  auto r1 = foo();
  auto r2 = foo();
  cout << "foo= " << r1 << " " << (void*)r1 << endl;
  cout << "bar= " << r2 << " " << (void*)r2 << endl;
  return 0;
}
