import logging
import re

_CAMEL_PATTERN = re.compile(r"(?<!^)(?=[A-Z])")


def get_logger(name="gather_client_ws", log_level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def camel_to_snake(s):
    return _CAMEL_PATTERN.sub("_", s).lower()


def snake_to_camel(s):
    pascal_case = "".join(word.title() for word in s.split("_"))
    return pascal_case[0].lower() + pascal_case[1:]
