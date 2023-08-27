from typing import Optional

from pydantic import BaseModel


class TodoCreate(BaseModel):
    id: int
    text: Optional[str]
    is_active: bool
