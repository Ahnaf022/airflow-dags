from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def say_hello():
    print("Hello from Airflow! This DAG came from GitHub.")

with DAG(
    dag_id="hello_github",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
):
    hello = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
