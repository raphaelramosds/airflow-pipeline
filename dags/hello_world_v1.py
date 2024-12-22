"""
v1 : hello world with object DAG
"""
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

dag_object = DAG (
    dag_id = "hello_world_v1",
    start_date = datetime(2024, 12, 22),
    schedule="@daily",
)

start = EmptyOperator(task_id="start", dag = dag_object)
hello = BashOperator(task_id="hello", bash_command="echo hello world", dag = dag_object)
end = EmptyOperator(task_id="end", dag = dag_object)

start >> hello >> end