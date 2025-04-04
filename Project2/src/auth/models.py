from sqlmodel import SQLModel, Field, Column
from sqlalchemy.sql import func  # Import func from sqlalchemy.sql
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users_accounts"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            default=uuid.uuid4,
        )
    )
    username: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    is_verified: bool = Field(default=False)
    email: str = Field(
        sa_column=Column(pg.VARCHAR, unique=True, nullable=False),  # Fixed type to VARCHAR
    )
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, server_default=func.now()),  # Use func.now() for default timestamp
    )

    def __repr__(self) -> str:
        return (
            f"User(uid={self.uid}, username={self.username}, first_name={self.first_name}, "
            f"last_name={self.last_name}, email={self.email})"
        )