from typing import Any
from pydantic import BaseModel , Field , ConfigDict

class ModelDeployment(BaseModel):
    """Represents a configured connection to an LLM provider"""

    model_config = ConfigDict(extra="forbid")

    deployment_id: str = Field(min_length=1)
    model_alias: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    provider_model: str = Field(min_length=1)
    api_base: str | None = None
    credential_reference: str = Field(min_length=1)
    timeout: float = Field(default=30.0, gt=0)
    weight: int = Field(default=1, gt=0)
    enabled: bool = True
    max_concurrent_requests: int | None = Field(
        default=None,
        gt=0,
    )
    retry_policy: dict[str, Any] = Field(default_factory=dict)
    fallback_priority: int = Field(default=0, ge=0)
