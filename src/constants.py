import os
from enum import Enum

API_ID: str = os.getenv("API_ID")
API_HASH: str = os.getenv("API_HASH")
CHAT_NAME: str = os.getenv("CHAT_NAME")
CHAT_FORWARD_LIST: list = os.getenv("CHAT_FORWARD_LIST").split(",")


class Constants(Enum):
    API_ID = API_ID
    API_HASH = API_HASH
    CHAT_NAME = CHAT_NAME
    CHAT_FORWARD_LIST = CHAT_FORWARD_LIST
