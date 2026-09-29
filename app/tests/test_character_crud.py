from crud.characters import CharacterCrud
from db import SessionLocal

def test_character_creation():
  with SessionLocal.begin() as session:
    crud = CharacterCrud(session)
    character = crud.add(name='Grimma', level=1, gold=5)
    session.flush()
    assert character.id is not None