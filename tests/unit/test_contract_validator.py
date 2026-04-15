from incentive_fraud.contracts.validator import validate_claim_event

def test_validate_claim_event_success():
    payload = {"event_id":"evt-1","event_type":"claims.submitted","event_ts":"2026-01-01T10:00:00Z","claim_id":"clm-1","claimant_id":"cust-1","partner_id":"partner-1","reseller_id":"reseller-1","program_id":"prog-1","sku_id":"sku-1","purchase_date":"2025-12-28","rebate_amount":99.0,"currency":"USD","country_code":"US"}
    result = validate_claim_event(payload)
    assert result.is_valid is True

def test_validate_claim_event_fails_negative_amount():
    payload = {"event_id":"evt-1","event_type":"claims.submitted","event_ts":"2026-01-01T10:00:00Z","claim_id":"clm-1","claimant_id":"cust-1","partner_id":"partner-1","reseller_id":"reseller-1","program_id":"prog-1","sku_id":"sku-1","purchase_date":"2025-12-28","rebate_amount":-1.0,"currency":"USD","country_code":"US"}
    result = validate_claim_event(payload)
    assert result.is_valid is False
