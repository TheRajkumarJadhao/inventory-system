from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

item_vendor = Table(
    "item_vendor",
    Base.metadata,
    Column("item_id", Integer, ForeignKey("stock_items.id")),
    Column("vendor_id", Integer, ForeignKey("vendors.id"))
)

class StockItem(Base):
    __tablename__ = "stock_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    vendors = relationship("Vendor", secondary=item_vendor, back_populates="items")

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    contact_info = Column(String)

    items = relationship("StockItem", secondary=item_vendor, back_populates="vendors")

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("stock_items.id"))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    quantity = Column(Integer)

    item = relationship("StockItem")
    vendor = relationship("Vendor")
