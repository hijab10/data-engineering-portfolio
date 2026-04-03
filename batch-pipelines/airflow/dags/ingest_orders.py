from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add scripts folder to path
sys.path.append("/opt/airflow/scripts") 

from load_transactions import main as load_data


default_args = {
    "owner": "hijab",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="ingest_orders",
    default_args=default_args,
    schedule=None,  # manual trigger
    catchup=False,
    description="Load online retail dataset into Postgres",
) as dag:

    ingest_task = PythonOperator(
        task_id="load_raw_transactions",
        python_callable=load_data,
        execution_timeout=timedelta(minutes=10),
    )

    ingest_task