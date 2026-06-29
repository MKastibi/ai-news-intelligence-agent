from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Category(str, Enum):
    LLMS = "LLMs"
    AGENTS = "Agents"
    REGULATION = "Regulation"
    ROBOTICS = "Robotics"
    AI_TOOLS = "AI Tools"
    SECURITY = "Security"
    OTHER = "Other"


@dataclass
class ArticleAnalysis:
    title: str
    impact_score: int
    category: Category
    companies: List[str]
    audience: str
    opportunity: str

    def __post_init__(self) -> None:
        if not 1 <= self.impact_score <= 10:
            raise ValueError(f"impact_score must be 1-10, got {self.impact_score}")


@dataclass
class AnalysisResult:
    analyses: List[ArticleAnalysis] = field(default_factory=list)
