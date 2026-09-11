from pathlib import Path

from openai import AsyncOpenAI

from bot.config import Config


class LlmClient:
    def __init__(self, config: Config) -> None:
        self._model = config.llm_model
        self._system_prompt = Path("prompts/system.txt").read_text(encoding="utf-8")
        self._client = AsyncOpenAI(
            base_url=config.llm_base_url,
            api_key=config.llm_api_key,
        )

    async def ask(self, user_text: str) -> str:
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": user_text},
            ],
        )
        return response.choices[0].message.content or ""
