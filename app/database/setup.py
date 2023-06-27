from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abhi8477@0.tcp.in.ngrok.io:10392/Test"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()