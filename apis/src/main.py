import uvicorn
from fastapi import FastAPI, Depends
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

class RequestBoard(BaseModel):
    title: str
    content: Optional[str] = None


class ResponseBoard(BaseModel):
    id: str
    title: str
    content: Optional[str] = None

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get('/boards', response_model=List[ResponseBoard])
async def get_boards(db: Session = Depends(get_db)):
    boards = db.query(models.Board).all()
    return boards


@app.post('/boards', response_model=ResponseBoard)
async def add_boards(req: RequestBoard, db: Session = Depends(get_db)):
    boards = models.Board(**req.dict())

    db.add(boards)

    db.commit()

    return boards


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
