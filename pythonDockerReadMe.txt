Python Docker container configuration.

The idea is to separate development environment from the workspace.
So we will add volume to the docker container with the present working directory to mapApp
This will then save all our python codes on local computer and will not dispapear after we close the container.

om@om:~/Documents/Github/Makpython/pythonWorkspace$ sudo docker run -it -v $PWD:/makApp python /bin/bash



Ready to use jupyternotebook datascience docker image

sudo docker pull jupyter/datascience-notebook:ubuntu-22.04

https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html

$sudo docker images
REPOSITORY                     TAG            IMAGE ID       CREATED         SIZE
jupyter/datascience-notebook   ubuntu-22.04   6d522ceccd36   2 days ago      4.56GB

docker run -it -p 8888:8888 6d52



pip freeze > requirements.txt

requirement.txt Contetnts
##############
python-dateutil==2.8.2
six==1.16.0
######################

Share projects between developer

consume a project
pip install -r requirements.txt

e

pip install python-dateutil===1.4

pip install "python-dateutil==2.7.*" --upgrade

pip uninstall python-dateutil

pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
