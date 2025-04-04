from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.sql import text
from src.config import Config
from sqlmodel import SQLModel  # Import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

# Use create_async_engine for AsyncEngine
engine: AsyncEngine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
)

async def initdb():
    """Initialize the database."""
    async with engine.begin() as conn:
        # Execute a simple query to create all tables
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    """Provide a database session."""
    async_session = sessionmaker(
        bind=engine,  # Use the correct engine variable
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session