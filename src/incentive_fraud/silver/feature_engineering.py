from __future__ import annotations
from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F

def build_features(claims: DataFrame) -> DataFrame:
    claimant_window = Window.partitionBy("claimant_id").orderBy(F.col("ingest_ts").cast("long"))
    partner_window = Window.partitionBy("partner_id")
    return (claims.withColumn("claim_rank_for_claimant", F.row_number().over(claimant_window))
        .withColumn("claim_count_by_partner", F.count("*").over(partner_window))
        .withColumn("avg_partner_rebate_amount", F.avg("rebate_amount").over(partner_window))
        .withColumn("is_amount_outlier", F.when(F.col("rebate_amount") > F.col("avg_partner_rebate_amount") * 2.5, True).otherwise(False))
        .withColumn("risk_score", (F.when(F.col("is_high_amount_claim"), 40).otherwise(0) + F.when(F.col("claim_rank_for_claimant") > 3, 20).otherwise(0) + F.when(F.col("is_amount_outlier"), 30).otherwise(0)))
        .withColumn("risk_band", F.when(F.col("risk_score") >= 60, "high").when(F.col("risk_score") >= 30, "medium").otherwise("low")))
