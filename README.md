# BIG DATA Analytics 
Welcome to the BigData Analytics repository! This repository is designed to provide you with hands-on experience and practical instructions for working with various Big Data tools and technologies. This setup will create Docker containers with the following frameworks: HDFS, HBase, Hive, Spark, Jupyter, Hue, MongoDB, Kafka, MySQL, and Zookeeper:

## REQUIRED SOFTWARE

To create and use the environment, we will use Git and Docker:
* Install Docker Desktop on Windows [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows) or Docker on [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

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

#### In a terminal/DOS, within the docker directory, clone the project from GitHub:

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
