from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemCreate(Item):
    pass

class ItemResponse(Item):
    id: int

    class Config:
        from_attributes = True