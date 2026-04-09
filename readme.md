# 📦 Multi-Vendor Inventory System

## 🚀 Overview

This project is a **FastAPI-based backend service** for managing inventory with a **many-to-many relationship between items and vendors**. It supports stock tracking, vendor linking, and a controlled ordering system.

---

## ✨ Features

* 📊 **Stock Management**
  Maintain a centralized list of inventory items.

* 🤝 **Vendor Management**
  Link multiple vendors to a single item.

* 🛒 **Ordering System**
  Create purchase orders with vendor selection.

* ✅ **Validation Rules**
  Orders can only be placed with vendors linked to the item.

* 🔗 **REST API Endpoints**

  * `POST /items/` → Create item
  * `GET /items/` → List items
  * `POST /vendors/` → Create vendor
  * `POST /vendors/link/{item_id}/{vendor_id}` → Link vendor
  * `POST /orders/` → Create order
  * `GET /orders/` → List orders

---

## 🛠️ Tech Stack

* **FastAPI** – API framework
* **SQLAlchemy** – ORM
* **PostgreSQL** – Database
* **Pytest** – Testing

---

## 📁 Project Structure

```bash
app/
├── main.py          # FastAPI entry point
├── database.py      # Database connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── routers/
│   ├── stock.py     # Item endpoints
│   ├── vendor.py    # Vendor endpoints
│   └── orders.py    # Order endpoints

tests/
├── test_items.py
├── test_vendors.py
└── test_orders.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/inventory-system.git
cd inventory-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Database

```sql
CREATE DATABASE inventory_db;
```

### 4️⃣ Configure Connection

Update in `database.py`:

```python
DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/inventory_db"
```

### 5️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

### 6️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

### 7️⃣ Run Tests

```bash
pytest -v
```

---

## 🧩 ER Diagram

```
+-----------+        +-------------+        +-------------+
| StockItem |<------>| ItemVendor  |<------>| Vendor      |
+-----------+        +-------------+        +-------------+
      |                                         ^
      |                                         |
      +-------------< PurchaseOrder >------------+
```

* **StockItem ↔ Vendor** → Many-to-Many (via ItemVendor)
* **PurchaseOrder** → Links item + vendor + quantity

---


## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---




