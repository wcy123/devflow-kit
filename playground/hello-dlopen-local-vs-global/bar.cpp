
extern "C" const char* common() { return "bar"; }

extern "C" const char* hello() { return common(); }
