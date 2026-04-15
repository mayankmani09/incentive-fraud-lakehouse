from __future__ import annotations
from pyspark.sql import functions as F
from incentive_fraud.bronze.iceberg_writer import configure_spark, write_to_iceberg
from incentive_fraud.contracts.quarantine import write_quarantine
from incentive_fraud.contracts.validator import validate_claim_event
from incentive_fraud.observability.otel import configure_tracing, get_tracer
from incentive_fraud.utils.io import read_jsonl
from incentive_fraud.utils.metrics import pipeline_stage_duration_seconds
INPUT_PATH = "data/generated/events/claims_submitted.jsonl"
TABLE_NAME = "bronze_claim_events"

def main() -> None:
    configure_tracing("bronze-claims-job")
    tracer = get_tracer(__name__)
    with tracer.start_as_current_span("contract_validation"):
        raw_records = read_jsonl(INPUT_PATH)
        valid_records, invalid_records = [], []
        for record in raw_records:
            result = validate_claim_event(record)
            if result.is_valid:
                valid_records.append(record)
            else:
                invalid_records.append({"record": record, "violations": [v.model_dump() for v in result.violations]})
        if invalid_records:
            write_quarantine(invalid_records, "data/quarantine/claims_invalid.jsonl")
    with pipeline_stage_duration_seconds.labels("bronze_ingestion").time():
        spark = configure_spark("bronze-claims-job")
        df = spark.createDataFrame(valid_records)
        df = df.withColumn("ingest_ts", F.current_timestamp()).withColumn("source_system", F.lit("synthetic_claim_generator")).withColumn("contract_status", F.lit("validated"))
        write_to_iceberg(df, TABLE_NAME)
        spark.stop()

if __name__ == "__main__":
    main()
