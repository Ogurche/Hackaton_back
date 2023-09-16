from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import get_key
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

DATABASE_URL = get_key(dotenv_path, 'DB_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
