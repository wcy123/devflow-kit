

all: run

main: main.cpp
	g++ -o $@ -g -O0 $< -ldl

libfoo.so: foo.cpp libcommon.so
	g++  -fPIC -shared -g -O0 -o $@ $< -lcommon1 -L.

libbar.so: bar.cpp libcommon.so
	g++ -fPIC -shared -g -O0 -o $@ $< -lcommon1 -L.

libcommon.so: common.cpp
	g++ -fPIC -shared -g -O0 -o $@ $<

libcommon1.so: common.cpp
	g++ -DCOMMON=\"c1\" -fPIC -shared -g -O0 -o $@ $<

libcommon2.so: common.cpp
	g++ -DCOMMON=\"c2\" -fPIC -shared -g -O0 -o $@ $<

run: main libcommon1.so libcommon2.so libfoo.so libbar.so
	./main  libfoo.so libbar.so
