from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.post("/", response_model=schemas.VendorBase)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(database.get_db)):
    new_vendor = models.Vendor(**vendor.dict())
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor

@router.post("/link/{item_id}/{vendor_id}")
def link_vendor(item_id: int, vendor_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.StockItem).get(item_id)
    vendor = db.query(models.Vendor).get(vendor_id)
    item.vendors.append(vendor)
    db.commit()
    return {"message": "Vendor linked successfully"}
