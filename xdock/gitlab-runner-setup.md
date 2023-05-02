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
% sudo env ALL_PROXY=socks5h://localhost:10080 curl -vL --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/v11.10.0/binaries/gitlab-runner-linux-amd64
% ls -l /usr/local/bin/gitlab-runner
% sudo chmod +x /usr/local/bin/gitlab-runner
% sudo useradd --comment 'GitLab Runner' --home-dir /scratch/gitlab-runner --create-home gitlab-runner --shell /bin/bash
% sudo gitlab-runner install --user=chunywan --working-directory=/scratch
% sudo gitlab-runner start
% sudo gitlab-runner status
% sudo gitlab-runner stop
% sudo gitlab-runner uninstall
% sudo gitlab-runner register --help
% sudo gitlab-runner start --help
% sudo gitlab-runner  --help
% sudo gitlab-runner run --help
% sudo gitlab-runner run "--working-directory" "/scratch" "--config" "/etc/gitlab-runner/config.toml"
% sudo gitlab-runner list
% sudo rm /etc/gitlab-runner/config.toml
% sudo cat /etc/gitlab-runner/config.toml
% sudo systemctl status gitlab-runner
% sudo cat /etc/systemd/system/gitlab-runner.service
% cd /home;
% sudo mkdir gitlab-runner
% sudo chown gitlab-runner:gitlab-runnner
% sudo usermod -d /home/gitlab-runner gitlab-runner
% curl -v -H 'User-Agent: gitlab-runner 11.10.0 (11-10-stable; go1.8.7; linux/amd64)' \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{"info":{"name":"gitlab-runner","version":"11.10.0","revision":"3001a600","platform":"linux","architecture":"amd64","executor":"docker","shell":"bash","features":{"variables":true,"image":true,"services":true,"artifacts":true,"cache":true,"shared":false,"upload_multiple_artifacts":true,"upload_raw_artifacts":true,"session":true,"terminal":true,"refspecs":true,"masking":true}},"token":"hrHRNS_HyWWoETJCTTsm"}' \
      http://xcdl190260/api/v4/jobs/request
```

register a runner

``` console
% sudo gitlab-runner register --non-interactive \
  --name "xcdsda29 for aisw" \
  --url "http://xcdl190260/" \
  --registration-token "BfuCWMasbGssXa-vED96" \
  --executor "docker" \
  --docker-image "xdock.xilinx.com/vitis-ai-cpu:1.3.593" \
  --ssh-user "gitlab-runner" \
  --ssh-host "localhost" \
  --ssh-port "22" \
  --ssh-identity-file "/scratch/gitlab-runner/.ssh/id_rsa" \
  --tag-list "aisw,u280,xcdsda29" \
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

```
FATAL: Failed to start gitlab-runner: "systemctl" failed: exit status 5, Failed to start gitlab-runner.service: Unit not found.
```
