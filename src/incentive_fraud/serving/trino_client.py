from __future__ import annotations
import trino
from incentive_fraud.config import settings

def get_connection():
    return trino.dbapi.connect(host=settings.trino_host, port=settings.trino_port, user=settings.trino_user, catalog="iceberg", schema="default")
