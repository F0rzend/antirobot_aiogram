from typing import Union, Optional

from loguru import logger
from sys import stderr  # stdin, stdout or stderr


def setup_logger(level: Union[str, int] = 'DEBUG', colorize: Optional[bool] = True):
    logger.remove()
    logger.add(sink=stderr, level=level, colorize=colorize, enqueue=True)
    logger.info("Логгирование успешно настроено\n")
