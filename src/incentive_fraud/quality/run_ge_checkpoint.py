from __future__ import annotations
try:
    import great_expectations as gx
except Exception:
    gx = None
from incentive_fraud.utils.metrics import dq_failed_total

def main() -> None:
    if gx is None:
        print("Great Expectations not installed or not initialized. Skipping real checkpoint execution.")
        return
    context = gx.get_context()
    checkpoint = context.get_checkpoint("silver_claims_checkpoint")
    result = checkpoint.run()
    if not result.success:
        dq_failed_total.inc()
        raise RuntimeError("Data quality checks failed")

if __name__ == "__main__":
    main()
