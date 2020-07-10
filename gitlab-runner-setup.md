# install gitlab runner




``` console
% ssh -R10022:localhost:22 xcdsda29
% lsb_release -a
% ssh  -D 10080 -p 10022 localhost
```

refer to https://docs.gitlab.com/runner/install/linux-manually.html

``` console
% ssh xcdsda29
% alias sudo=/tools/xgs/bin/sudo
% sudo curl -vL --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64
% ls -l /usr/local/bin/gitlab-runner
% sudo chmod +x /usr/local/bin/gitlab-runner
% sudo useradd --comment 'GitLab Runner' --home-dir /scratch/gitlab-runner --create-home gitlab-runner --shell /bin/bash
% sudo gitlab-runner install --user=gitlab-runner --working-directory=/scratch/gitlab-runner
% sudo gitlab-runner start
```

register a runner

``` console
% sudo gitlab-runner register --non-interactive \
  --url "http://xcdl190260/" \
  --registration-token "tE176x4k6z-FPiHDYaDK" \
  --executor "ssh" \
  --ssh-user "gitlab-runner" \
  --ssh-host "localhost" \
  --ssh-port "22" \
  --ssh-identity-file "/scratch/gitlab-runner/.ssh/id_rsa" \
  --description "ssh-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"
% sudo /usr/local/bin/gitlab-runner restart
```


# create cross compilation for sdk


## microblaze sdk

``` console
% ssh gitlab-user@xcdsda29
% mkdir -p $HOME/build
% cd $HOME/build
% scp xcdl190253:/tmp/for_chunye_mb/sdk.sh mb_sdk.sh # todo put the sdk in a wellknown place
% ./mb_sdk.sh -y -d $(realpath $HOME/build/mb_sdk)
% # /var/lib/docker/scratch/gitlab-runner/build/mb_sdk/environment-setup-microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux
```

## petalinux zcu102

``` console
% ssh gitlab-user@xcdsda29
% mkdir -p $HOME/build
% cd $HOME/build
% ls  /group/dphi_software/software/petalinux_sdk/sdk-0618.sh
% scp chunywan@xcdl190253:/group/dphi_software/software/petalinux_sdk/sdk-0618.sh .
% ./sdk-0618.sh -d sdk-0618 -y
%
```
