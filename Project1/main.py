from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

#serach in list

userList = ["John", "Jane", "Doe"]

@app.get("/search")
async def search(user:str):
    if(user in userList):
        return {"message": f"{user} found!"}
    else:
        return {"message": f"{user} not found!"}
    

@app.get("/options")
async def options(name:Optional[str]="Vinay"):
    return {"message": f"Hello, {name}!"}


class Item(BaseModel):
    name: str
    age: int
    description: Optional[str] = None

@app.post("/items")
async def create_item(item: Item):
    return {"item": item}
