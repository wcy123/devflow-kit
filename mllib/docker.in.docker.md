

see https://devopscube.com/run-docker-in-docker/

```
ssh -p 10022 localhost
```

```
ssh localhost curl --unix-socket /var/run/docker.sock http://localhost/version
# edit mount_dir.whitelist
ls -l /var/run/ | grep docker
curl --unix-socket /var/run/docker.sock http://localhost/version
```

```

sudo -E apt-get update
sudo -E apt-get install -y docker.io
docker ps
dpkg -L docker wmdocker
sudo -E apt-get install -y apt-file
sudo -E apt-file update
```
