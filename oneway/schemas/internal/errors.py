from typing import Any
from pydantic import BaseModel , ConfigDict , Field

class LLMErrors(BaseModel):
    """Standarized LLM errors"""
    model_config = ConfigDict(extra='forbid',arbitrary_types_allowed=True)

    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    provider: str | None = None
    deployment_id: str | None = None
    http_status: int | None = Field(
        default=None,
        ge=100,
        le=599,
    )
    retryable: bool = False
    retry_after: float | None = Field(
        default=None,
        ge=0,
    )
    original_exception: Any | None = None