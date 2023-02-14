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
