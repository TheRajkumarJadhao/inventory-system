from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/inventory_db"
#I have used local postgress for this project

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        print("Database session opened.")
        yield db
    finally:
        print("Database session closed.")
        db.close()

get_db()