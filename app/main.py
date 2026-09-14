from models import Base, Character
from db import engine, SessionLocal

def app():
  Base.metadata.create_all(engine)

  with SessionLocal() as session:
    character = Character(
      name='Gorak',
      level=1,
      gold=50
    )

    session.add(character)
    session.commit()

if __name__ == '__main__':
  app()