from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderBase)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    new_order = models.PurchaseOrder(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=list[schemas.OrderResponse])
def list_orders(db: Session = Depends(database.get_db)):
    return db.query(models.PurchaseOrder).all()
