from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., max_length=20)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='Author age should be more than 15')

class AuthorOut(Author):
    id: int

    # @validator('age')
    # def check_age(cls, v):
    #     if v<15:
    #         raise ValueError('Author age should be more than 15')
    #     return v


class Books(BaseModel):
    title:  str
    writer: str
    duration: str
    price: float
    summary: str=None
    date: date
    genre: List[Genre]
