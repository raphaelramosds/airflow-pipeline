from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import pendulum
import pprint

"""
Task que imprime um nome estatico utilizando pprint

Observação:
 - Assim como o BashOperator define a task como um comando do bash
   o PythonOperator define a task como uma função do python
"""
def meu_codigo(**kwargs):
    print("andre")
    pprint.pprint(kwargs)
    return 123

with DAG (
    dag_id="python_operator_v1",
    schedule="* * * * *", # Executar a cada minuto (notação do cron tab)
    start_date=pendulum.datetime(2024,12,22,14,10,tz="America/Recife"),
    catchup=True
) as dag:
    start = EmptyOperator(task_id="start")
    python = PythonOperator(task_id="python", python_callable=meu_codigo)
    end = EmptyOperator(task_id="end")

start >> python >> end