from dataclasses import dataclass
from typing import Optional


@dataclass
class Article:
    title: str
    link: str
    summary: str
    source: str
    published_at: Optional[str] = None
