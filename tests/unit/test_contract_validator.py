from incentive_fraud.contracts.models import ClaimSubmitted, ContractViolation, ValidationResult
from incentive_fraud.contracts.validator import validate_claim_event


def _valid_payload(**overrides):
    payload = {
        "event_id": "evt-1",
        "event_type": "claims.submitted",
        "event_ts": "2026-01-01T10:00:00Z",
        "claim_id": "clm-1",
        "claimant_id": "cust-1",
        "partner_id": "partner-1",
        "reseller_id": "reseller-1",
        "program_id": "prog-1",
        "sku_id": "sku-1",
        "purchase_date": "2025-12-28",
        "rebate_amount": 99.0,
        "currency": "USD",
        "country_code": "US",
    }
    payload.update(overrides)
    return payload


def test_validate_claim_event_success():
    result = validate_claim_event(_valid_payload())
    assert result.is_valid is True


def test_validate_claim_event_fails_negative_amount():
    result = validate_claim_event(_valid_payload(rebate_amount=-1.0))
    assert result.is_valid is False


def test_validate_claim_event_fails_invalid_event_type():
    result = validate_claim_event(_valid_payload(event_type="claimsXsubmitted"))
    assert result.is_valid is False


def test_validate_claim_event_fails_missing_required_field():
    payload = _valid_payload()
    payload.pop("sku_id")
    result = validate_claim_event(payload)
    assert result.is_valid is False


def test_model_defaults_are_not_shared_between_instances():
    first_claim = ClaimSubmitted(**_valid_payload())
    second_claim = ClaimSubmitted(**_valid_payload(event_id="evt-2", claim_id="clm-2"))

    first_claim.metadata["source"] = "first"
    assert "source" not in second_claim.metadata

    first_result = ValidationResult(is_valid=False)
    second_result = ValidationResult(is_valid=False)
    first_result.violations.append(
        ContractViolation(contract_name="claims_submitted", reason="x", payload={})
    )
    assert len(second_result.violations) == 0
