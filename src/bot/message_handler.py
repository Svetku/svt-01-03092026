import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.llm_client import LlmClient

logger = logging.getLogger(__name__)


class MessageHandler:
    def __init__(self, llm_client: LlmClient) -> None:
        self._llm = llm_client
        self.router = Router()
        self.router.message.register(self.on_start, CommandStart())
        self.router.message.register(self.on_text, F.text)

    async def on_start(self, message: Message) -> None:
        logger.info("/start chat_id=%s", message.chat.id)
        await message.answer("Бот на связи. Напиши вопрос.")

    async def on_text(self, message: Message) -> None:
        try:
            reply = await self._llm.ask(message.text or "")
        except Exception:
            logger.exception("LLM request failed chat_id=%s", message.chat.id)
            await message.answer("Сейчас ответить не получилось. Попробуй ещё раз.")
            return
        await message.answer(reply)
