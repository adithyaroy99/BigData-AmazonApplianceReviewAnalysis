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

## Setup Instructions
1. Clone the repository
2. Start Docker containers via `docker-compose up -d`
3. Access the namenode container and load data into HDFS
4. Run Spark jobs for data processing and model training

## Repository Structure
- `/data` - datasets and input files
- `/scripts` - data processing and ML scripts
- `/docker` - docker-compose and service configuration files

## References
This project is completed using the environmental setup made from the BigDataCourse repository by [Usman Akhtar](https://github.com/usmanakhtar/BigDataCourse)
