# Airflow 

## O que é Apache Airflow?

- O Airflow é um sistema de gerenciamento de fluxo de trabalho de código aberto de alto nível para programas orientados por DAGs (Directed Acyclic Graphs). 
- As DAGs possuem tarefas (tasks) que são executadas em uma ordem definida
- O Airflow permite que os usuários criem, documentem, planejem e gerenciem tarefas e fluxos de trabalho complexos.

## Arquitetura

O *Apache Airflow* é organizado com os seguintes componentes

- **Scheduler** agenda as DAGS e envia das tasks para os *workers*
- **Executor** executa as tarefas
- **Web server** apresenta uma interface para o usuário gerenciar as DAGs e as tasks
- **DAGs folder** armazena as DAGs criadas pelo usuário
- **Metadados** banco de dados que atende como um repositório da ferramenta, utilizados pelo Executor e Scheduler para guardar os estados da aplicação

### DAGs

DAGs são as sequencias de tarefas não cíclicas controladas pelo Airflow. Isso quer dizer que uma tarefa não pode chamar ela mesma.

Uma tarefa pode ser comandos do bash, do python, etc. 

O que vai definir a natureza de uma tarefa é a classe Operator que a define. Abaixo estão alguns exemplos.

- BashOperator permite que a task execute comandos do bash
- PythonOperator permite que a task execute comandos do python

## Referencias

[1] [Dependência entre DAGs](https://www.youtube.com/watch?v=MvjTQNMRhhY)

[2] [Apache Airflow Tutoital](https://www.youtube.com/playlist?list=PLLNidqMOzeD5yXv9lDtBM-VJ5-1F-ZdXI)