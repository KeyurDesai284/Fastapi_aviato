from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./GCP.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # Create the engine
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False) # Create local session
Base = declarative_base() # Use to create classes or database model (ORM Model)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()