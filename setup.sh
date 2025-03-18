#!/bin/bash

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y docker.io docker-compose openjdk-11-jdk python3-pip

# Install Apache Kafka
wget https://downloads.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz
tar -xvzf kafka_2.13-3.0.0.tgz
mv kafka_2.13-3.0.0 kafka
cd kafka

# Start Kafka
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &

# Install Apache Spark
cd ..
wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar -xvzf spark-3.1.2-bin-hadoop3.2.tgz
mv spark-3.1.2-bin-hadoop3.2 spark

# Install Apache Airflow
pip3 install apache-airflow

# Start Airflow Scheduler & Webserver
airflow db init
airflow scheduler &
airflow webserver -p 8080 &

echo "Setup Complete!"
