# Airflow Pipeline

## O que é Airflow?

O Airflow é um sistema de gerenciamento de fluxo de trabalho de código aberto de alto nível para programas orientados por DAGs (Directed Acyclic Graphs). 

As DAGs possuem tarefas (tasks) que são executadas em uma ordem definida

O Airflow permite que os usuários criem, documentem, planejem e gerenciem tarefas e fluxos de trabalho complexos.

## Arquitetura

O *Apache Airflow* é organizado com os seguintes componentes

- *Scheduler* agenda as DAGS e envia das tasks para os *workers*
- *Executor* executa as tarefas
- *Web server* é uma interface para o usuário gerenciar as DAGs e as tasks
- *DAGs folder* armazena as DAGs criadas pelo usuário
- *Metadados* banco de dados que atende como um repositório da ferramenta, utilizados pelo Executor e Scheduler para guardar os estados da aplicação