# BigData-AmazonApplianceReviewAnalysis

## Project Overview
This project implements a Big Data analytics framework using Hadoop and Spark to analyze large-scale customer reviews of home appliances. It includes environment setup with Docker containers, data ingestion into HDFS, data processing with Spark, and machine learning modeling with PySpark MLlib.

## Features
- Dockerized Hadoop, Spark, and related services for easy environment setup
- Data ingestion and processing pipelines for appliance customer reviews
- ML model implementation for sentiment analysis or review classification
- Detailed documentation and best practices for Big Data workflows

## Requirements
- Docker Desktop  
- Git  
- WSL (for Windows users)  
- Python 3.x  
- PowerShell (for Windows users)

## Setup Instructions

**Note:** This setup should be performed only once. After creating the environment, use `docker-compose` to manage services.

### 1. Create the Docker Working Directory

- **Windows:**  
  Create the `docker` directory at the root of your drive.  
  Example: `C:\docker`

- **Linux/Mac:**  
  Create the directory in your home folder.  
  Example: `/home/user/docker`

### 2. Clone the Repository
```bash
git clone https://github.com/adithyaroy99/BigData-AmazonApplianceReviewAnalysis.git
cd BigData-AmazonApplianceReviewAnalysis
```

### 3. Start Docker Services
```bash
docker-compose up -d
```
To stop all services:
```bash
docker-compose down
```

### 4. Access Hadoop Namenode Container
```bash
docker exec -it namenode bash
```
Disable safemode:
```bash
hadoop dfsadmin -safemode leave
```

### 5. Upload Dataset Files to HDFS

- Create a directory in HDFS:
  ```bash
  hdfs dfs -mkdir -p /data/appliances
  ```
- Upload the review and metadata files:
  ```bash
  hdfs dfs -put /data/Appliances.jsonl /data/appliances/
  hdfs dfs -put /data/meta_Appliances.jsonl /data/appliances/
  ```
- Verify upload:
  ```bash
  hdfs dfs -ls /data/appliances/
  ```

(Optional) Access the Namenode browser UI at [http://localhost:55070/](http://localhost:55070/) to check the `/data/appliances` folder.

### 6. Launch Jupyter Notebook

- Access Jupyter-Spark: [http://localhost:8889/](http://localhost:8889/)
- Open the notebook:  
  `Amazon Appliances Review Analysis with Spark (PySpark) and Hadoop.ipynb`
- Run all cells to reproduce the analysis workflow.

## Dataset Access

Due to large size, datasets are **not** included in this repository.  
Please download the **Amazon Reviews 2023** dataset (Appliances category) from:  
[https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/)

## References

This project is completed using the environmental setup made from the BigDataCourse repository by [Usman Akhtar](https://github.com/usmanakhtar/BigDataCourse).
