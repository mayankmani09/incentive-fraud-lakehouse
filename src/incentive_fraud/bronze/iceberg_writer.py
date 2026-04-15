from __future__ import annotations
from pyspark.sql import DataFrame, SparkSession

def configure_spark(app_name: str = "iceberg-writer") -> SparkSession:
    return (SparkSession.builder.appName(app_name)
        .config("spark.sql.catalog.demo", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.demo.type", "hadoop")
        .config("spark.sql.catalog.demo.warehouse", "s3a://warehouse/")
        .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
        .config("spark.hadoop.fs.s3a.access.key", "minio")
        .config("spark.hadoop.fs.s3a.secret.key", "miniostorage")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .getOrCreate())

def write_to_iceberg(df: DataFrame, table_name: str, mode: str = "append") -> None:
    writer = (df.writeTo(f"demo.default.{table_name}").option("merge-schema", "true").using("iceberg").tableProperty("format-version", "2"))
    if mode == "append":
        writer.append()
    else:
        writer.createOrReplace()
