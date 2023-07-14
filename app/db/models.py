from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    username: str
    company: str
    email: str
    password: str

