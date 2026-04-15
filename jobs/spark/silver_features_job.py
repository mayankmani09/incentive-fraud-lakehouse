from __future__ import annotations
from incentive_fraud.bronze.iceberg_writer import configure_spark, write_to_iceberg
from incentive_fraud.observability.otel import configure_tracing, get_tracer
from incentive_fraud.silver.feature_engineering import build_features
from incentive_fraud.utils.metrics import claims_flagged_total, claims_processed_total, pipeline_stage_duration_seconds

def main() -> None:
    configure_tracing("silver-features-job")
    tracer = get_tracer(__name__)
    with tracer.start_as_current_span("feature_engineering"):
        with pipeline_stage_duration_seconds.labels("silver_features").time():
            spark = configure_spark("silver-features-job")
            claims = spark.read.format("iceberg").load("demo.default.silver_claims")
            features = build_features(claims)
            claims_processed_total.inc(features.count())
            claims_flagged_total.inc(features.filter("risk_band = 'high'").count())
            write_to_iceberg(features, "silver_claim_risk_features")
            spark.stop()

if __name__ == "__main__":
    main()
