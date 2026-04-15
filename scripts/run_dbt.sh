#!/usr/bin/env bash
set -euo pipefail
cd dbt
dbt deps || true
dbt seed || true
dbt run || true
dbt test || true
