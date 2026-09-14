from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv(
  'DATABASE_URL',
  'postgresql+psycopg://postgres:password@localhost:5432/quest_board'
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)