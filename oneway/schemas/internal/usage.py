
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class TokenUsage(BaseModel):
    """Normalized token usage across all LLM providers."""

    model_config = ConfigDict(extra="forbid")

    prompt_tokens: int = Field(ge=0)

    completion_tokens: int = Field(ge=0)

    total_tokens: int = Field(ge=0)

    source: Literal["provider", "estimated"]
