# Inside main.py title
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import initdb

#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    print("Server is starting...")
    yield
    print("Server is shutting down...")



version = 'v1'

app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
    lifespan=lifespan
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])