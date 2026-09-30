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
  session.flush()
  
  return character

@pytest.fixture
def crud(session: Session):
  return CharacterCrud(session)

def test_character_creation(crud: CharacterCrud):
  found_character = crud.add(name='Grimma', level=1, gold=5)
  assert found_character.id is not None

def test_get_character(crud: CharacterCrud, character: Character):
  character = crud.get(id=character.id)

  assert character.id is not None
  assert character.name == 'Grimma'
  assert character.level == 1
  assert character.gold == 5

def test_list_characters(crud: CharacterCrud, character):
  characters = crud.list()
  assert character in characters

def test_update_character(crud: CharacterCrud, character: Character):
  crud.update(id=character.id, name='Lah Ghar', level=2, gold=100)

  updated_character = crud.get(id=character.id)

  assert updated_character
  assert updated_character.name == 'Lah Ghar'
  assert updated_character.level == 2
  assert updated_character.gold == 100

def test_delete_character(crud: CharacterCrud, character: Character):
  crud.delete(id=character.id)

  deleted_character = crud.get(id=character.id)

  assert deleted_character is None
  