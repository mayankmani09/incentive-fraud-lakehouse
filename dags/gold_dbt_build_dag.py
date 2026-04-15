from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(dag_id="gold_dbt_build_dag", start_date=datetime(2026,1,1), schedule=None, catchup=False) as dag:
    dbt_run = BashOperator(task_id="dbt_run", bash_command="cd /opt/project/dbt && dbt run")
    dbt_test = BashOperator(task_id="dbt_test", bash_command="cd /opt/project/dbt && dbt test")
    dbt_run >> dbt_test
