select * from {{ ref("fct_claim_fraud_signals") }} where rebate_amount <= 0
