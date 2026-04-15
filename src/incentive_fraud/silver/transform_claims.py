from __future__ import annotations
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def transform_claims(df: DataFrame) -> DataFrame:
    return (df.dropDuplicates(["event_id"]).withColumn("claim_date", F.to_date("purchase_date")).withColumn("is_high_amount_claim", F.when(F.col("rebate_amount") >= 750, F.lit(True)).otherwise(F.lit(False))))
