from typing import List

import requests

from app.core.config import Config
from app.core.exceptions import APIError

TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"
MAX_MESSAGE_LENGTH = 4096
REQUEST_TIMEOUT = 15


def _split_message(text: str, max_length: int = MAX_MESSAGE_LENGTH) -> List[str]:
    parts: List[str] = []
    while len(text) > max_length:
        split_at = text.rfind("\n", 0, max_length)
        if split_at == -1:
            split_at = text.rfind(". ", 0, max_length)
        if split_at == -1:
            split_at = max_length
        parts.append(text[:split_at].strip())
        text = text[split_at:].strip()
    if text:
        parts.append(text)
    return parts


def send_telegram_message(text: str) -> None:
    url = TELEGRAM_API_URL.format(token=Config.telegram_bot_token)
    payload = {
        "chat_id": Config.telegram_chat_id,
        "parse_mode": "Markdown",
    }

    parts = _split_message(text)
    for i, part in enumerate(parts):
        payload["text"] = part
        try:
            response = requests.post(url, json=payload, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.RequestException as e:
            raise APIError(
                f"Failed to send Telegram message part {i + 1}/{len(parts)}: {e}"
            ) from e
