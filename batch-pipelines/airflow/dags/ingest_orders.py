from datetime import datetime, timedelta
import logging
import sys

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

sys.path.append("/opt/airflow/scripts")
from load_transactions import main as load_data


def run_ingestion():
    logging.info("Starting ingestion")
    load_data()
    logging.info("Finished ingestion")


with DAG(
    dag_id="ingest_orders",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "owner": "hijab",
        "retries": 1,
    },
    description="Load online retail CSV into Postgres",
) as dag:
    PythonOperator(
        task_id="load_raw_transactions",
        python_callable=run_ingestion,
        execution_timeout=timedelta(minutes=10),
    )