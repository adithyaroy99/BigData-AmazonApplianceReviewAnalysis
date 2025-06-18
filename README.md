# BIG DATA ECOSYSTEM WITH DOCKER

Environment for studying the main big data frameworks in Docker.
This setup will create Docker containers with the following frameworks: HDFS, HBase, Hive, Spark, Jupyter, Hue, MongoDB, Kafka, MySQL, and Zookeeper:

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
    Example: C:\docker

* Suggestion for Linux:
  * Create the directory in the user's home.
    Example: /home/user/docker

#### In a terminal/DOS, within the docker directory, clone the project from GitHub:

```bash
git clone https://github.com/usmanakhtar/BigDataCourse.git

