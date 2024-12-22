from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule='@daily', catchup=False)
def dag_a():

	@task
	def task_a():
		print("task_a")

	task_a()

dag_a()