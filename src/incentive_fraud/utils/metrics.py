from __future__ import annotations
from prometheus_client import Counter, Histogram
claims_processed_total = Counter("claims_processed_total", "Total number of claims processed")
claims_flagged_total = Counter("claims_flagged_total", "Total number of claims flagged")
dq_failed_total = Counter("dq_failed_total", "Total number of data quality failures")
pipeline_stage_duration_seconds = Histogram("pipeline_stage_duration_seconds", "Duration of pipeline stages in seconds", ["stage_name"])
