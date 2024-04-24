from ray import serve
from ray.serve.handle import DeploymentHandle
from starlette.requests import Request
from transformers import pipeline


@serve.deployment
class Summarizer:
    def __init__(self, translator: DeploymentHandle):
        # Load model
        self.translator = translator
        self.model = pipeline("summarization", model="t5-small")

    def summarize(self, text: str) -> str:
        # Run inference
        model_output = self.model(text, min_length=5, max_length=15)

        # Post-process output to return only the summary text
        summary = model_output[0]["summary_text"]
        return summary

    async def __call__(self, request: Request) -> str:
        english_text: str = await request.json()
        summary = self.summarize(english_text)
        translation = await self.translator.translate.remote(summary)
        return translation
