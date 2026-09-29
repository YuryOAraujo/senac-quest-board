import pytest

from models import Character
from crud.characters import CharacterCrud
from sqlalchemy.orm import Session
from db import SessionLocal

@pytest.fixture
def session():
  session = SessionLocal()

  try:
    yield session
  finally:
    session.rollback()
    session.close()

@pytest.fixture
def character(session: Session):
  character = Character(name='Grimma', level=1, gold=5)

  session.add(character)
  session.commit()

  return character

def test_character_creation(session: Session):
  crud = CharacterCrud(session)
  character = crud.add(name='Grimma', level=1, gold=5)
  assert character.id is not None

def test_get_character(session: Session, character: Character):
  crud = CharacterCrud(session)
  character = crud.get(id=character.id)
  assert character.id is not None

def test_list_characters(session: Session):
  crud = CharacterCrud(session)
  characters = crud.list()
  assert len(characters) >= 1

def test_update_character(session: Session, character: Character):
  crud = CharacterCrud(session)
  crud.update(id=character.id, name='Lah Ghar', level=2, gold=100)

  updated_character = crud.get(id=character.id)

  assert updated_character
  assert updated_character.name == 'Lah Ghar'
  assert updated_character.level == 2
  assert updated_character.gold == 100

def test_delete_character(session: Session, character: Character):
  crud = CharacterCrud(session)
  crud.delete(id=character.id)

  deleted_character = crud.get(id=character.id)

  assert deleted_character is None
  