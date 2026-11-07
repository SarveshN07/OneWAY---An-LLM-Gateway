from pydantic import BaseModel , Field , ConfigDict
from typing import Any,Literal

class Message(BaseModel):
    """Represents an individual conversation message"""

    model_config = ConfigDict(extra="forbid")

    role = Literal["system","user","assitant"]
    content : str


class LLMRequest(BaseModel):
    """Provider-independent representation of an LLM request"""
    model_config = ConfigDict(extra="forbid")

    model : str = Field(min_length=1)
    messages : list[Message] = Field(min_length=1)
    temperature : float | None = Field(
        default=None,
        ge=0,
        le=2
    )
    max_tokens = int | None = Field(
        default=None,
        ge= 0
    )
    top_p : float | None  = Field(
        default=None,
        gt = 0,
        le = 1
    )
    stop : list[str] | None = None
    stream : bool = False
    tools : list[dict[str,Any]] | None = None