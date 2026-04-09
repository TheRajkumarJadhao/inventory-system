# Multi-Vendor Inventory System

## Overview
This project is a **FastAPI backend service** designed to manage a product inventory where items have a many-to-many relationship with vendors. It supports stock tracking, vendor management, and a flexible ordering flow.

## Features
- **Stock Management**  
  Maintain a central registry of unique stock items.
- **Vendor Relations**  
  Link multiple vendors to a single item.
- **Ordering Logic**  
  Create purchase orders with manual vendor selection.
- **Validation**  
  Ensure orders can only be placed with linked vendors.
- **API Endpoints**
  - `POST /items/` → Create a new item
  - `GET /items/` → List all items
  - `POST /vendors/` → Create a new vendor
  - `POST /vendors/link/{item_id}/{vendor_id}` → Link vendor to item
  - `POST /orders/` → Create a new order
  - `GET /orders/` → List all orders


## Tech Stack
- **FastAPI** (REST API framework)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (Database)
- **Pytest** (Testing)

## Project Structure
app/
├── main.py          # FastAPI entry point
├── database.py      # Database connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── routers/
│    ├── stock.py    # Item endpoints
│    ├── vendor.py   # Vendor endpoints
│    └── orders.py   # Order endpoints
tests/
├── test_items.py
├── test_vendors.py
└── test_orders.py



## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-system.git
   cd inventory-system

# install requierments
2. pip install -r requirements.txt

# Create DB
3. CREATE DATABASE inventory_db;

# Create Connection
4. DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/inventory_db"

# Run Server
5. uvicorn main:app --reload

# Swagger UI
6. http://127.0.0.1:8000/docs

# Testing
7. pytest -v

# ER Diagram

+-----------+        +-------------+        +-------------+
| StockItem |<------>| ItemVendor  |<------>| Vendor      |
+-----------+        +-------------+        +-------------+
      |                                         ^
      |                                         |
      +-------------< PurchaseOrder >------------+


StockItem ↔ Vendor: Many-to-many via ItemVendor

PurchaseOrder: Links an item to a vendor with quantity

