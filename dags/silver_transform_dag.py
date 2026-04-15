from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(dag_id="silver_transform_dag", start_date=datetime(2026,1,1), schedule=None, catchup=False) as dag:
    transform_claims = BashOperator(task_id="transform_claims", bash_command="python /opt/project/jobs/spark/silver_claims_job.py")
    generate_features = BashOperator(task_id="generate_features", bash_command="python /opt/project/jobs/spark/silver_features_job.py")
    transform_claims >> generate_features
