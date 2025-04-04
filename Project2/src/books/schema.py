from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class Book(BaseModel):
    uid: UUID  # Change from int to UUID
    title: str
    author: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime  # Change from str to datetime
    updated_at: datetime  # Change from str to datetime

    class Config:
        orm_mode = True  # Enable compatibility with ORM models

class BookCreateModel(BaseModel):
    title: str
    author: str
    published_date: str
    page_count: int
    language: str    

class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None