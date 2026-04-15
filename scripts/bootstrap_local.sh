#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
pip install -r requirements.txt
mkdir -p data/generated/events data/generated/reference data/quarantine logs
echo "Local bootstrap complete"
