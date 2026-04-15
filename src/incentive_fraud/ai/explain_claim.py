from __future__ import annotations
import argparse
from incentive_fraud.ai.bedrock_provider import BedrockLLMProvider
from incentive_fraud.ai.local_provider import LocalLLMProvider
from incentive_fraud.ai.prompts import EXPLAIN_CLAIM_PROMPT
from incentive_fraud.ai.retriever import load_corpus
from incentive_fraud.config import settings

def get_provider():
    return BedrockLLMProvider() if settings.llm_provider == "bedrock" else LocalLLMProvider()

def build_claim_context(claim_id: str) -> str:
    return f"claim_id={claim_id}; risk_score=70; risk_band=high; repeated claimant submissions; partner baseline deviation; sku/program mismatch suspected"

def main(claim_id: str) -> None:
    provider = get_provider()
    prompt = EXPLAIN_CLAIM_PROMPT.format(claim_context=build_claim_context(claim_id), policy_context=load_corpus()[:1500], historical_context="Prior cases with shared payment fingerprint and partner spike were escalated.")
    try:
        print(provider.generate(prompt))
    except Exception:
        print("Explanation unavailable. Review manually.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--claim-id", required=True)
    args = parser.parse_args()
    main(args.claim_id)
