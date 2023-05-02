extern "C" const char* common() { return "foo"; }
extern "C" const char* hello() { return common(); }
