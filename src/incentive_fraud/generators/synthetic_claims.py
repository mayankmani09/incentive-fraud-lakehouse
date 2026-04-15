from __future__ import annotations
import json, random
from datetime import datetime, timedelta, timezone
from pathlib import Path
from faker import Faker
fake = Faker()

def generate_claim_event(idx: int, suspicious: bool = False) -> dict:
    now = datetime.now(timezone.utc)
    rebate_amount = round(random.uniform(25, 500), 2)
    claimant_id = f"claimant-{random.randint(1, 100)}"
    partner_id = f"partner-{random.randint(1, 20)}"
    reseller_id = f"reseller-{random.randint(1, 50)}"
    sku_id = f"sku-{random.randint(1, 100)}"
    if suspicious:
        rebate_amount *= 4
        claimant_id = "claimant-7"
        partner_id = "partner-3"
        sku_id = "sku-99"
    return {
        "event_id": f"evt-{idx}", "event_type": "claims.submitted", "event_ts": now.isoformat(),
        "claim_id": f"clm-{idx}", "claimant_id": claimant_id, "partner_id": partner_id,
        "reseller_id": reseller_id, "program_id": f"program-{random.randint(1, 10)}", "sku_id": sku_id,
        "purchase_date": (now - timedelta(days=random.randint(1, 30))).date().isoformat(),
        "rebate_amount": round(rebate_amount, 2), "currency": random.choice(["USD", "CAD"]),
        "country_code": random.choice(["US", "CA"]), "payment_account_fingerprint": f"payfp-{random.randint(1, 30)}",
        "device_fingerprint": f"devfp-{random.randint(1, 40)}", "metadata": {"channel": random.choice(["dealer_portal", "partner_api", "mobile_app"]), "submission_ip": fake.ipv4_public()}
    }

def main(output_dir: str = "data/generated/events", n: int = 500) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    records = [generate_claim_event(i, suspicious=(i % 33 == 0)) for i in range(1, n + 1)]
    with open(Path(output_dir) / "claims_submitted.jsonl", "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

if __name__ == "__main__":
    main()
