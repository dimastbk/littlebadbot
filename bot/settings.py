import logging
import os

from dotenv import load_dotenv

load_dotenv()

# Настройки бота
BOT_ADMIN = os.getenv('BOT_ADMIN', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
BOT_PROXY = os.getenv('BOT_PROXY', '')

# Настройки redis
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)

REDIS_SOCKET = os.getenv('REDIS_SOCKET', '')

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
