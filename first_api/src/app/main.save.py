from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


### Handle version from .version ###
version = "0.0.0"
try:
    with open('.version') as reader:
        version = reader.read()
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

######

app = FastAPI(version=version)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}