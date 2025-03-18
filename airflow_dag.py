from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

def train_deep_learning_model():
    subprocess.run(['python', 'deep_learning_model.py'])

def run_spark_processing():
    subprocess.run(['spark-submit', 'spark_processing.py'])

def start_kafka_streaming():
    subprocess.run(['python', 'kafka_streaming.py'])

# Define DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'heart_disease_pipeline',
    default_args=default_args,
    schedule_interval='@daily'
)

# Define Tasks
train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_deep_learning_model,
    dag=dag
)

spark_task = PythonOperator(
    task_id='process_big_data',
    python_callable=run_spark_processing,
    dag=dag
)

kafka_task = PythonOperator(
    task_id='start_kafka',
    python_callable=start_kafka_streaming,
    dag=dag
)

# Define task dependencies
train_task >> spark_task >> kafka_task
