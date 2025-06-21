# BIG DATA Analytics 
Welcome to the BigData Analytics repository! This repository is designed to provide you with hands-on experience and practical instructions for working with various Big Data tools and technologies. This setup will create Docker containers with the following frameworks: HDFS, HBase, Hive, Spark, Jupyter, Hue, MongoDB, Kafka, MySQL, and Zookeeper:

## REQUIRED SOFTWARE

To create and use the environment, we will use Git and Docker:
* Install Docker Desktop on Windows [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) or Docker on [Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Make sure WSL is installed properly and docker is in running state. 

## SETUP

*Note: This step should be performed only once. After creating the environment, use docker-compose to start the containers as shown in the topic STARTING THE ENVIRONMENT.*

#### Creating the Docker Directory:

*Note: Create a directory called docker.*

* Suggestion for Windows:
  * Create the docker directory at the root of your drive.
    Open PowerShell Example: C:\docker

* Suggestion for Mac:
  * Create the directory in the user's home.
   Terminal Example: /home/user/docker

#### Open the Powershell, clone the project from GitHub:

```bash
git clone https://github.com/usmanakhtar/BigDataCourse.git
```

## Docker
After cloning the project 
```bash
cd BigDataCourse
```
To start all the services using the docker
```bash
docker-compose up -d 
```
To stop all services
```bash
docker-compose down 
```
Further changes in the ```bash Docker-compose.yml``` file
After installation you need to change the image from fjardim/namenode_sqoop to usmanakhtar17/bigdatacourse:namenode. Secondly you need to create a /Workspace folder you need to the update the path of your folder location.

```bash
  namenode:
    #image: fjardim/namenode_sqoop
    #build: .
    image: usmanakhtar17/bigdatacourse:namenode
    container_name: namenode
    hostname: namenode
    volumes:
      - ./data/hdfs/namenode:/hadoop/dfs/name
      - /c/Users/uakhtar/Docker-images/BigDataCourse/bigdata_docker/Workspace:/Workspace 
```


### Hadoop Setup (MapReduce Streaming)

First step is to go to the namenode container from terminal. 

```bash
docker exec -it namenode bash 
```
Make sure to disable the namenode from safemode operation

```bash
hadoop dfsadmin -safemode leave
```


hadoop fs -mkdir -p /home/datasrc/bigDataTask

hadoop fs -put pessoas.csv /home/datasrc/bigDataTask

hadoop fs -ls /home/datasrc/bigDataTask

Path: 
df = spark.read.csv('hdfs://namenode:8020/home/datasrc/bigDataTask/pessoas.csv', header=True, inferSchema=True)
