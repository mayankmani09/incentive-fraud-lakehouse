from incentive_fraud.ai.prompts import EXPLAIN_CLAIM_PROMPT

def test_prompt_contains_claim_context_placeholder():
    assert "{claim_context}" in EXPLAIN_CLAIM_PROMPT
