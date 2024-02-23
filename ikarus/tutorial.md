# tutorial

download [tutorial](https://github.com/namin/inc/blob/master/docs/tutorial.pdf?raw=true)

http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf

# download source code

```
cd /workspace
git clone https://github.com/namin/inc.git
cd /workspace/inc/src; ls -l
```

```
sudo -E apt-get install -y gcc-multilib g++-multilib
```

# ex 1

```
cd /workspace/inc/src; ls -l
bat tests-1.1-req.scm;
bat tests-driver.scm
bat ctest.c
bat startup.c

scheme
(load "tests-driver.scm")
all-tests
(load "tests-1.1-req.scm")
all-tests
(test-all)

```
