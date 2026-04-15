from __future__ import annotations
from incentive_fraud.bronze.iceberg_writer import configure_spark, write_to_iceberg
from incentive_fraud.observability.otel import configure_tracing, get_tracer
from incentive_fraud.silver.transform_claims import transform_claims
from incentive_fraud.utils.metrics import pipeline_stage_duration_seconds

def main() -> None:
    configure_tracing("silver-claims-job")
    tracer = get_tracer(__name__)
    with tracer.start_as_current_span("silver_claim_transform"):
        with pipeline_stage_duration_seconds.labels("silver_claims").time():
            spark = configure_spark("silver-claims-job")
            bronze = spark.read.format("iceberg").load("demo.default.bronze_claim_events")
            silver = transform_claims(bronze).select("event_id","claim_id","claimant_id","partner_id","reseller_id","program_id","sku_id","claim_date","rebate_amount","currency","country_code","payment_account_fingerprint","device_fingerprint","ingest_ts","is_high_amount_claim")
            write_to_iceberg(silver, "silver_claims")
            spark.stop()

if __name__ == "__main__":
    main()
