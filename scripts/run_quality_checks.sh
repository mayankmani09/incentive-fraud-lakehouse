#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src python -m incentive_fraud.quality.run_ge_checkpoint || true
