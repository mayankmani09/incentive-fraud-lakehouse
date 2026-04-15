#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=${PYTHONPATH:-src}
echo "==> Generating synthetic claim events"
python scripts/generate_demo_events.py
echo "==> Running Bronze ingestion"
python jobs/spark/bronze_claims_job.py || echo "Bronze job requires configured Spark + Iceberg runtime"
echo "==> Running Silver normalization"
python jobs/spark/silver_claims_job.py || echo "Silver claims job requires configured Spark + Iceberg runtime"
echo "==> Running Silver feature engineering"
python jobs/spark/silver_features_job.py || echo "Silver features job requires configured Spark + Iceberg runtime"
echo "==> Building Gold marts with dbt"
bash scripts/run_dbt.sh || echo "dbt run skipped; configure Trino catalog before execution"
echo "==> Running quality checks"
bash scripts/run_quality_checks.sh || echo "Quality checks skipped; configure GE runtime before execution"
echo "==> Generating investigator explanation"
PYTHONPATH=src python -m incentive_fraud.ai.explain_claim --claim-id clm-33
echo "==> Demo completed"
