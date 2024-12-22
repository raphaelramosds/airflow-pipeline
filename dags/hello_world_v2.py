"""
v2 : hello world with decorator
"""
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag (
    start_date = datetime(2024, 12, 22),
    schedule="@daily",
)

def hello_world():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")
    start >> hello >> end

create_dag = hello_world()