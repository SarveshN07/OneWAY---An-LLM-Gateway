from pydantic import BaseModel , Field , ConfigDict
from datetime import datetime, timezone
from oneway.schemas.internal.usage import TokenUsage



class LLMResponse(BaseModel):
    """Provider-independent representation of an LLM response."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    model: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    deployment_id: str = Field(min_length=1)
    content: str
    finish_reason: str | None = None
    usage: TokenUsage
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
