"""
v0 : hello world
"""
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG (
    dag_id = "hello_world_v0",
    start_date = datetime(2024, 12, 22),
    schedule="@daily",
):
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")

(start >> hello >> end)