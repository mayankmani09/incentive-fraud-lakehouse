from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "local")
    warehouse_bucket: str = os.getenv("WAREHOUSE_BUCKET", "warehouse")
    raw_bucket: str = os.getenv("RAW_BUCKET", "lakehouse")
    s3_endpoint_url: str = os.getenv("S3_ENDPOINT_URL", "http://localhost:9000")
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    trino_host: str = os.getenv("TRINO_HOST", "localhost")
    trino_port: int = int(os.getenv("TRINO_PORT", "8080"))
    trino_user: str = os.getenv("TRINO_USER", "trino")
    llm_provider: str = os.getenv("LLM_PROVIDER", "local")
    vector_store_dir: str = os.getenv("VECTOR_STORE_DIR", ".vectorstore")

settings = Settings()
