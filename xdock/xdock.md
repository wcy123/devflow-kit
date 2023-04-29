

```
sudo chgrp docker /var/run/docker.sock
sudo systemctl start docker
make ftp_server
docker rm "/squid-container"
docker run -d --name squid-container -e TZ=UTC -p 3128:3128 ubuntu/squid:4.13-21.10_edge
```


```
ssh -R9181:localhost:3128 -J xcdl190074 xcdl190252
while sleep 1; do echo xcoengvm229033; done
```


```
ssh -R9181:localhost:3128 -J xcdl190074 xcdl190253
while sleep 1; do echo xcoengvm229033; done
```
