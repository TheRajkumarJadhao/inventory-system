from fastapi import FastAPI
from .routers import stock, vendor, orders
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multi-Vendor Inventory System")

app.include_router(stock.router)
app.include_router(vendor.router)
app.include_router(orders.router)
