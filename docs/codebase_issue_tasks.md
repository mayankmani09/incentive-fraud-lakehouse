# Codebase Issue Triage Tasks

## 1) Typo fix task: correct the `event_type` regex pattern

**Issue found:** In the `ClaimSubmitted` model, `event_type` uses `Field(pattern="claims.submitted")`, where `.` is a regex wildcard instead of a literal period. That makes values like `claimsXsubmitted` match unexpectedly.

**Task proposal:** Replace the pattern with an anchored, escaped literal like `^claims\.submitted$`.

**Why this is a typo task:** This is a one-character regex typo (`.` vs `\.`) that changes validation semantics.

**Suggested acceptance criteria:**
- The model only accepts `claims.submitted`.
- Inputs such as `claims-submitted` and `claimsXsubmitted` are rejected.

---

## 2) Bug fix task: remove mutable default values in Pydantic models

**Issue found:** `ClaimSubmitted.metadata` is initialized with `{}` and `ValidationResult.violations` with `[]`. Mutable class defaults can cause shared state across model instances.

**Task proposal:** Replace these with `Field(default_factory=dict)` and `Field(default_factory=list)`.

**Suggested acceptance criteria:**
- Two fresh `ClaimSubmitted` instances do not share `metadata`.
- Two fresh `ValidationResult` instances do not share `violations`.

---

## 3) Documentation discrepancy task: align architecture docs with quality-gate scope

**Issue found:** The README architecture diagram implies quality checks are tied to the Gold layer (`E -. checks .-> I[Great Expectations / Soda]`), while configured checks target Silver claims datasets (`silver_claims_checkpoint.yml` and `silver_claims_scan.yml`).

**Task proposal:** Update the architecture docs to reflect the current implementation (Silver quality gates), or extend checks/configuration so Gold quality checks are actually present.

**Suggested acceptance criteria:**
- README diagram and operations/docs text explicitly reflect the implemented quality-gate layer(s).
- If keeping the Gold claim, add concrete Gold checks and reference them in docs.

---

## 4) Test improvement task: strengthen contract validator tests for schema strictness

**Issue found:** Current tests cover success and negative rebate amount only; they do not test `event_type` strictness, malformed payloads, or mutable-default isolation.

**Task proposal:** Expand `tests/unit/test_contract_validator.py` to include:
- a failing test for non-literal `event_type` values,
- a failing test for missing required fields,
- an isolation test ensuring repeated validation results do not share `violations` state.

**Suggested acceptance criteria:**
- New tests fail on current behavior (where applicable) and pass after fixes.
- Test names clearly map to contract rules and regression risk.
