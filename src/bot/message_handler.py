import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

logger = logging.getLogger(__name__)


class MessageHandler:
    def __init__(self) -> None:
        self.router = Router()
        self.router.message.register(self.on_start, CommandStart())

    async def on_start(self, message: Message) -> None:
        logger.info("/start chat_id=%s", message.chat.id)
        await message.answer("Бот на связи. Напиши вопрос.")
