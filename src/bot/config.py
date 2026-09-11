import os

from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        load_dotenv()
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set")
        self.telegram_bot_token = token
