from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task, dag
import pendulum
import pprint

@dag (
    schedule="* * * * *", # Executar a cada minuto (notação do cron tab)
    start_date=pendulum.datetime(2024,12,22,14,26,tz="America/Recife"),
    catchup=True
)

def python_operator_v2():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    @task(task_id="python")
    def meu_codigo(ds=None, **kwargs):
        pprint.pprint(kwargs)
        print(ds)
        return "meu retorno agora é esse texto"    

    python = meu_codigo()

    start >> python >> end

python_operator_v2()