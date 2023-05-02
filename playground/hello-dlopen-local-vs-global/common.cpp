#ifndef COMMON
#define COMMON "common"
#endif

extern "C" const char* common() __attribute__((weak));
extern "C" const char* common() { return COMMON; }
extern "C" const char* hello() { return common(); }
