import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.dialog_memory import DialogMemory
from bot.llm_client import LlmClient

logger = logging.getLogger(__name__)


class MessageHandler:
    def __init__(self, llm_client: LlmClient, memory: DialogMemory) -> None:
        self._llm = llm_client
        self._memory = memory
        self.router = Router()
        self.router.message.register(self.on_start, CommandStart())
        self.router.message.register(self.on_reset, Command("reset"))
        self.router.message.register(self.on_text, F.text)

    async def on_start(self, message: Message) -> None:
        logger.info("/start chat_id=%s", message.chat.id)
        await message.answer("Бот на связи. Напиши вопрос.")

    async def on_reset(self, message: Message) -> None:
        logger.info("/reset chat_id=%s", message.chat.id)
        self._memory.reset(message.chat.id)
        await message.answer("История этого чата очищена.")

    async def on_text(self, message: Message) -> None:
        chat_id = message.chat.id
        self._memory.add(chat_id, "user", message.text or "")
        try:
            reply = await self._llm.ask(self._memory.get(chat_id))
        except Exception:
            logger.exception("LLM request failed chat_id=%s", chat_id)
            await message.answer("Сейчас ответить не получилось. Попробуй ещё раз.")
            return
        self._memory.add(chat_id, "assistant", reply)
        await message.answer(reply)
