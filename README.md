# Makpython

All the files in this repo are stored under app folder.
Then Jupyetr notebook is running on a docker container.
In thsi way the code is platform indepedent.

The docker container is in another repo.

To run the docker container use below command.
This will start the python container with Jupyter notebook and 
share the workspace of ~/Source/app

sudo docker run -v ~/Source/app:/myApp -p 8888:8888 om-python

To build the docker file,go to the folder where docker file is present and run:

sudo docker build -t om-python .

=======================================
Docker commands:
docker run - Run a command in a new container
docker start - Start one or more stopped containers
docker stop - Stop one or more running containers
docker build - Build an image from a Dockerfile
docker pull - Pull an image or a repository from a registry
docker push - Push an image or a repository to a registry
docker export - Export a container's filesystem as a tar archive
docker exec - Run a command in a running container
docker search - Search the Docker Hub for images
docker logs - Fetch the logs of a container
docker diff - Inspect changes to files or directories on a container's filesystem
Docker container management commands
docker ps - List containers
docker inspect - Display detailed information on one or more containers
docker top - Display the running processes of a container
docker port - List port mappings or a specific mapping for the container
docker stats - Display a live stream of container(s) resource usage statistics
Docker image management commands
docker images - List images
docker import - Import the contents from a tarball to create a filesystem image
docker history - Show the history of an image
docker tag - Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
docker rmi - Remove one or more images
