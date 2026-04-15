from __future__ import annotations
import boto3
from incentive_fraud.ai.provider import LLMProvider
class BedrockLLMProvider(LLMProvider):
    def __init__(self, model_id: str = "anthropic.claude-3-5-sonnet-20240620-v1:0") -> None:
        self.client = boto3.client("bedrock-runtime")
        self.model_id = model_id
    def generate(self, prompt: str) -> str:
        response = self.client.invoke_model(modelId=self.model_id, body=prompt.encode("utf-8"))
        return response["body"].read().decode("utf-8")
