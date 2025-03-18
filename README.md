# Heart_Disease_Detection

## Overview
This project implements a **heart disease prediction system** using **Deep Learning, Big Data Processing, Real-time Streaming, Cloud Deployment, and a Scalable API**. It includes:
- **Deep Learning Model** (TensorFlow/PyTorch) with **SHAP Explainability**.
- **Big Data Processing** using **Apache Spark**.
- **Real-time Streaming** via **Apache Kafka**.
- **Workflow Automation** using **Apache Airflow**.
- **Containerized Deployment** via **Docker & Kubernetes**.
- **Cloud Deployment** on **AWS & GCP** using **Terraform**.
- **Interactive Frontend** with real-time visualization.

---

## 📦 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/Heart_Disease_Detection.git
cd Heart_Disease_Detection
```

### **2️⃣ Install Dependencies**
Run the automated setup script to install **Docker, Kafka, Spark, and Airflow**.
```sh
chmod +x setup.sh
./setup.sh
```

### **3️⃣ Start Kafka & Streaming**  
```sh
cd kafka
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &
python kafka_streaming.py
```

### **4️⃣ Train the Deep Learning Model**  
```sh
python deep_learning_model.py
```

### **5️⃣ Start Spark Processing**
```sh
spark-submit spark_processing.py
```

### **6️⃣ Deploy API & Database with Docker**  
```sh
docker-compose up --build -d
```

### **7️⃣ Deploy to AWS/GCP (Optional)**  

#### **AWS Deployment**  
```sh
cd terraform
terraform init
terraform apply -auto-approve
```

#### **GCP Deployment**  
```sh
cd terraform_gcp
terraform init
terraform apply -auto-approve
```

#### **Kubernetes Deployment**  
```sh
kubectl apply -f kubernetes.yaml
```

### **8️⃣ Run Airflow Workflow**
```sh
airflow db init
airflow scheduler &
airflow webserver -p 8080 &
```

### **9️⃣ Start Frontend Dashboard**  
```sh
cd frontend
npm install
npm start
```

---

## 📊 **Components & Files**
| Component | File |
|-----------|------|
| **Deep Learning Model** | `deep_learning_model.py` |
| **Kafka Streaming** | `kafka_streaming.py`, `kafka_consumer.py` |
| **Spark Processing** | `spark_processing.py` |
| **Airflow DAGs** | `airflow_dag.py` |
| **Flask API** | `app.py` |
| **Database Setup** | `database.py` |
| **Encryption & Security** | `encryption.py` |
| **Docker Deployment** | `Dockerfile`, `docker-compose.yml` |
| **AWS Terraform** | `terraform_aws.tf` |
| **GCP Terraform** | `terraform_gcp.tf` |
| **Kubernetes Deployment** | `kubernetes.yaml` |
| **Automated Setup** | `setup.sh` |
| **Frontend Dashboard** | `frontend_dashboard.jsx` |

---

## 🚀 Future Enhancements
- Implement **Federated Learning** for better privacy.
- Optimize model performance with **Neural Architecture Search (NAS)**.
- Integrate **CI/CD Pipelines** for automated testing & deployment.

---

## 📢 Need Help?
Raise an issue on GitHub or reach out! 🎯
