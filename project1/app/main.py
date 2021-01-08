import models
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from routers import items
from database import SessionLocal, engine
from models import Items
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"Hello": "world"}

app.include_router(items.router, prefix="/items")


@app.post("/additem")
async def create_stock(item_request: str,db: Session = Depends(get_db)):
    item = Items()
    item.name = item_request
    db.add(item)
    db.commit()
    return {
        "code": "success",
        "message": "item was added to the database"
    }

@app.get("/all")
async def create_stock(db: Session = Depends(get_db)):
    items = db.query(Items)
    items = items.all()
    return items