from __future__ import annotations
from fastapi import FastAPI, Response
from prometheus_client import generate_latest
from incentive_fraud.ai.local_provider import LocalLLMProvider
app = FastAPI(title="Investigator API")
provider = LocalLLMProvider()

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.get("/metrics")
def metrics() -> Response:
    return Response(content=generate_latest(), media_type="text/plain")

@app.get("/claims/{claim_id}/explanation")
def explain_claim(claim_id: str) -> dict:
    return {"claim_id": claim_id, "explanation": provider.generate(f"Explain why claim {claim_id} may be suspicious.")}
