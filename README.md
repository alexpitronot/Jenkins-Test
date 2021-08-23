# Jenkins installation with Dockerfile

1. Build new network:
docker network create network_name
2. Run container for Jenkins network:
docker run --name container_name --rm --detach --privileged --network network_name --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2
3. Run Jenkins:
docker run --name container_name --rm --detach --network network_name --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro image_name
![image](https://user-images.githubusercontent.com/87993785/130457005-698310c7-2f23-464e-8c63-ab4f28fca093.png)


 
