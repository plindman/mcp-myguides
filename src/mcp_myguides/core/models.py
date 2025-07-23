from pydantic import BaseModel, Field, HttpUrl
from typing import List, Union

class GuideMetadata(BaseModel):
    id: str
    name: str
    description: str
    topics: List[str] = Field(default_factory=list)
    source: Union[str, HttpUrl]

class Guide(GuideMetadata):
    content: str
