from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(dag_id="bronze_ingestion_dag", start_date=datetime(2026,1,1), schedule="@hourly", catchup=False) as dag:
    generate_events = BashOperator(task_id="generate_events", bash_command="python /opt/project/scripts/generate_demo_events.py")
    ingest_bronze = BashOperator(task_id="ingest_bronze", bash_command="python /opt/project/jobs/spark/bronze_claims_job.py")
    generate_events >> ingest_bronze
