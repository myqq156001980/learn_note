# Dokcer command

> stop all the running docker ps

```
sudo docker stop $(sudo docker ps -a -q)
```

> rm all the bocker images

```
sudo docker rmi $(sudo docker images -q)
```

> rm all docker containers

```
sudo docker rm $(sudo docker ps -a -q)
```



