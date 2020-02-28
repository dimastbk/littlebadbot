import logging
import os

from dotenv import load_dotenv

load_dotenv()

# Настройки бота
BOT_ADMIN = os.getenv('BOT_ADMIN', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
BOT_PROXY = os.getenv('BOT_PROXY', '')

# Настроки команды /status
_service_list = os.getenv('STATUS_SERVICE_LIST')
STATUS_SERVICE_LIST = _service_list .split(',') if _service_list else None


# Настройки логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
