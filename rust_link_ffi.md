# rust ffi

``` console
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/learn
% cargo new --lib --name test-ffi test-ffi
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/learn/test-ffi; ls
% cargo build
% cargo test
% cat <<EOF
// add.c
int add(int a, int b) {
    return a + b;
}

EOF

% # edit build.srs
%  cargo build

```

``` c
// add.c
int add(int a, int b) {
    return a + b;
}

```
