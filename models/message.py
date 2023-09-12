from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id_trans: Optional[int]  #id transmitter
    id_rec: int             #id receiver
    text: str
    date: str