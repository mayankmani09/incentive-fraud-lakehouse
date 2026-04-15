from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class ClaimSubmitted(BaseModel):
    event_id: str
    event_type: str = Field(pattern="claims.submitted")
    event_ts: str
    claim_id: str
    claimant_id: str
    partner_id: str
    reseller_id: str
    program_id: str
    sku_id: str
    purchase_date: str
    rebate_amount: float
    currency: str
    country_code: str
    payment_account_fingerprint: Optional[str] = None
    device_fingerprint: Optional[str] = None
    metadata: Dict[str, Any] = {}

class ContractViolation(BaseModel):
    contract_name: str
    reason: str
    payload: Dict[str, Any]

class ValidationResult(BaseModel):
    is_valid: bool
    violations: List[ContractViolation] = []
