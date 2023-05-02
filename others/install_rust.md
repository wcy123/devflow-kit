#install rust


to avoid disk space problem

``` console
% mkdir -p /scratch/$USER/.cargo
% ln -s  /scratch/$USER/.cargo $HOME/
```

create proxy
``` console
% ssh -D10080 -p10152 localhost
```

``` console
% which rustup
% curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh  -s -- -v --version
rustup-init 1.22.0 (2d019878d 2020-07-02)

%  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | env RUSTUP_USE_CURL=1 ALL_PROXY=socks5h://localhost:10080 sh
# it is important to RUSTUP_USE_CURL=1, otherwise, proxy setting takes no effect.
```


``` console
% rustup component add rls rust-analysis rust-src
% cargo install racer
```


edit `~/.cargo/config`

``` console
[http]
proxy = "socks5h://localhost:10080"

[https]
proxy = "socks5h://localhost:10080"
```

# create rust mirror on xcdsda29

1. create a tunnel

``` console
% ssh -t -v  -R10022:localhost:10152 gitlab-runner@xcdsda29 ssh -v -p 10022 -D 10080 $USER@localhost
```

2. create an another session

see [python.md](python.md "python.md") about install pysocks. otherwise you got error as below

```
 Missing dependencies for SOCKS support
```


``` console
% ssh  gitlab-runner@xcdsda29
% export ALL_PROXY=socks5h://localhost:10080
% curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh  -s -- -v --version
% which pip3 # make sure it's $HOME/.local/pip3 , see python.md for more info
% pip3 install --proxy socks5h://localhost:10080 -r requirements.txt
% pip3 install --upgrade pip # optional
```


3. clone the crates io index

``` console
% mkdir -p $HOME/d/working; cd $HOME/d/working
% git clone https://github.com/rust-lang/crates.io-index.git
% cd $HOME/d/working/crates.io-index
% cat ./dx/va/dxva2-sys | jq .
% cat ./dx/va/dxva2-sys | jq -r '@sh "./update-crate \(.name) \(.vers) \(.cksum)"'
% git ls-tree -r --name-only HEAD .  | \
  xargs -n 1 -I % sh -c "cat % | jq -r '@sh \"./update-crate \(.name) \(.vers) \(.cksum)\"'" | bash -e
%
% ./update-crate 'dxva2-sys' '0.0.1' '8eb9e03f079ecdefa4ac1ab732c8d4fc594ec73151478f58bbe513c87e039a16'
% mkdir -p .cache
```

``` json
{
  "name": "dxva2-sys",
  "vers": "0.0.1",
  "deps": [
    {
      "name": "winapi",
      "req": "*",
      "features": [
        ""
      ],
      "optional": false,
      "default_features": true,
      "target": null,
      "kind": "normal"
    }
  ],
  "cksum": "8eb9e03f079ecdefa4ac1ab732c8d4fc594ec73151478f58bbe513c87e039a16",
  "features": {},
  "yanked": false
}
```
