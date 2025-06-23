

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
Further changes in the ```Docker-compose.yml``` file
After installation you need to change the image from ```fjardim/namenode_sqoop``` to ```usmanakhtar17/bigdatacourse:namenode```. Secondly you need to create a ```/Workspace``` folder you need to the update the path of your folder location.

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


## Hadoop Setup & (MapReduce Streaming)

First step is to go to the namenode container from terminal. 

```bash
docker exec -it namenode bash 
```
Make sure to disable the namenode from safemode operation

```bash
hadoop dfsadmin -safemode leave
```
#### 1. Hadoop Map/Reduce Jobs with Docker

First creata folder inside the HDFS
```bash
hadoop dfs -mkdir /Data
```
Now put the file inside the HDFS

```bash
hadoop dfs -put /Workspace/Example.txt /Data
```
To check the file exists inside the HDFS
```bash
hadoop dfs -ls  /Data
```
Now we will run the first MapReduce Job. You need to change directory from ```root@namenode:```

```bash
cd /opt/hadoop-2.7.4/share/hadoop/mapreduce
```
Now we will run the mapreduce job of wordcount. 

```bash
hadoop jar hadoop-mapreduce-examples-2.7.4.jar wordcound /Data/Eample.txt /Output1
```

#### 2. Hadoop Map/Reduce Jobs with Python

In this [tutorial](http://www.quuxlabs.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/), we will describe how to write a simple MapReduce program for Hadoop in the Python programming language. But i have edited the code based on our Hadoop Environment. Here are the updated files and place these file to Workspace folder. 

### `mapper.py`
```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    for word in line.split():
        print(f"{word}\t1")
```

### `reducer.py`
```python
#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word == word:
    print(f"{current_word}\t{current_count}")
```
Test the ```mapper``` and ```reducer``` function from namenode terminal make sure you run the following command from /Workspace folder.  
```bash
 echo "foo foo quux labs foo bar quux" | ./mapper.py
```
Sort and run the ```reducer``` function 
```bash
echo "foo foo quux labs foo bar quux" | ./mapper.py | sort | ./reducer.py
```
To run the MapReduce jobs in Python, we need to use the [Hadoop Streaming](https://hadoop.apache.org/docs/r1.2.1/streaming.html) that will run the MapReduce jobs. Run the following code:
```bash
hadoop jar /opt/hadoop-2.7.4/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar -files /Workspace/mapper.py,/Workspace/reducer.py -mapper mapper.py -reducer reducer.py -input /Data -output /Output3
```
to check the output of the MapReduce Job
```bash
hdfs dfs -ls /Output3
hdfs dfs -cat /Output3/part-00000
```
