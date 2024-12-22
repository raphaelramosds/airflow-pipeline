"""
DAG waiting for a

Executada diariamente quando a DAG 'dag_a' finalizar

"""

from airflow.decorators import dag, task
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule='@daily', catchup=False)
def waiting_for_a():

	waiting_for_a = ExternalTaskSensor(
		task_id='waiting_for_a',
		external_dag_id='dag_a',
		external_task_id='task_a'
	)

	@task
	def next_a():
		print("a")

	@task
	def done():
		print("done")

	waiting_for_a >> next_a() >> done()

waiting_for_a()