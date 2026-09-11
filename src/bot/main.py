import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


async def main() -> None:
    config = Config()
    bot = Bot(token=config.telegram_bot_token)
    dp = Dispatcher()
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
