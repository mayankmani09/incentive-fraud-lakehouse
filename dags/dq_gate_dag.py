import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
def check_quarantine():
    path = "data/quarantine/claims_invalid.jsonl"
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            count = sum(1 for _ in f)
        if count > 0:
            raise ValueError(f"Contract violations detected: {count}")
with DAG(dag_id="dq_gate_dag", start_date=datetime(2026,1,1), schedule=None, catchup=False) as dag:
    check_contracts = PythonOperator(task_id="check_contracts", python_callable=check_quarantine)
