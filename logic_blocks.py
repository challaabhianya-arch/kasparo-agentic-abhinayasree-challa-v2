from src.models import UserMessage
from src.responses import RESPONSES
from src.utils import contains
from src.config import EXIT_WORDS


def process_input(user_input: str) -> str:
    message = UserMessage(user_input)
    text = message.text

    if contains(text, "hello") or contains(text, "hi"):
        return RESPONSES["hello"]

    if contains(text, "name"):
        return RESPONSES["name"]

    if contains(text, "help"):
        return RESPONSES["help"]

    if any(word in text for word in EXIT_WORDS):
        return RESPONSES["bye"]

        return RESPONSES["default"]