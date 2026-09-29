import pytest

from crud.characters import CharacterCrud
from db import SessionLocal

@pytest.fixture
def session():
  session = SessionLocal()

  try:
    yield session
  finally:
    session.rollback()
    session.close()

def test_character_creation(session):
  crud = CharacterCrud(session)
  character = crud.add(name='Grimma', level=1, gold=5)
  assert character.id is not None