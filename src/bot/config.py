import os

from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        load_dotenv()
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set")
        self.telegram_bot_token = token

        base_url = os.getenv("LLM_BASE_URL")
        api_key = os.getenv("LLM_API_KEY")
        model = os.getenv("LLM_MODEL")
        if not base_url or not api_key or not model:
            raise ValueError("LLM_BASE_URL, LLM_API_KEY and LLM_MODEL must be set")
        self.llm_base_url = base_url
        self.llm_api_key = api_key
        self.llm_model = model
