from __future__ import annotations
import json, random
from datetime import datetime, timezone
from pathlib import Path

def main(output_dir: str = "data/generated/events", n: int = 200) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    path = Path(output_dir) / "partner_transactions.jsonl"
    now = datetime.now(timezone.utc)
    with open(path, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            record = {"transaction_id": f"txn-{i}", "partner_id": f"partner-{random.randint(1,20)}", "transaction_ts": now.isoformat(), "amount": round(random.uniform(100, 5000), 2)}
            f.write(json.dumps(record) + "\n")

if __name__ == "__main__":
    main()
