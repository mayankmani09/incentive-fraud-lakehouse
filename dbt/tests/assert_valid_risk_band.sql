select * from {{ ref("fct_claim_fraud_signals") }} where risk_band not in ("low", "medium", "high")
