from __future__ import annotations
from pydantic import ValidationError
from incentive_fraud.contracts.models import ClaimSubmitted, ContractViolation, ValidationResult

def validate_claim_event(payload: dict) -> ValidationResult:
    violations = []
    try:
        model = ClaimSubmitted(**payload)
    except ValidationError as exc:
        violations.append(ContractViolation(contract_name="claims_submitted", reason=str(exc), payload=payload))
        return ValidationResult(is_valid=False, violations=violations)
    if model.rebate_amount <= 0:
        violations.append(ContractViolation(contract_name="claims_submitted", reason="rebate_amount must be > 0", payload=payload))
    return ValidationResult(is_valid=len(violations) == 0, violations=violations)
