from __future__ import annotations
from incentive_fraud.ai.provider import LLMProvider
class LocalLLMProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return "Local demo explanation: The claim was flagged due to elevated rebate amount, repeated claimant behavior, and partner-level deviation from baseline."
