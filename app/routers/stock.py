from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=schemas.ItemBase)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    new_item = models.StockItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db: Session = Depends(database.get_db)):
    return db.query(models.StockItem).all()