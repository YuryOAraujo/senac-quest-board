import pytest

from crud.characters import CharacterCrud
from crud.quests import QuestCrud
from models import Character, Quest, CharacterQuest
from db import SessionLocal
from sqlalchemy.orm import Session

@pytest.fixture
def session():
  session = SessionLocal()

  try:
    yield session
  finally:
    session.rollback()
    session.close()

@pytest.fixture
def character_crud(session: Session) -> CharacterCrud:
  return CharacterCrud(session)

@pytest.fixture
def quest_crud(session: Session) -> CharacterCrud:
  return QuestCrud(session)

@pytest.fixture
def character(character_crud: CharacterCrud) -> Character:
  character = character_crud.add(name='Grimma', level=1, gold=50)
  return character

@pytest.fixture
def quest(quest_crud: QuestCrud) -> Quest:
  quest = quest_crud.add(title='First quest', description='Your journey starts here ...', rewards=100)
  return quest

@pytest.fixture
def assign_quest(character: Character, quest: Quest):
  character.assigned_quests.append(CharacterQuest(character.id, quest.id))
