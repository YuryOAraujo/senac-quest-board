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
  quest = quest_crud.add(title='First quest', description='Your journey starts here ...', reward=100)
  return quest

@pytest.fixture
def assigned_quest(session: Session, character: Character, quest: Quest):
  # character.assigned_quests.append(CharacterQuest(character_id=character.id, quest_id=quest.id))
  assigned_quest = CharacterQuest(character_id=character.id, quest_id=quest.id)
  session.add(assigned_quest)
  session.flush()

  return assigned_quest

def test_quest_assignment(session: Session, character: Character, quest: Quest, assigned_quest: CharacterQuest):
  found_assigned_quest = session.get(CharacterQuest, (character.id, quest.id))
  assert found_assigned_quest.character_id == assigned_quest.character_id
  assert found_assigned_quest.quest_id == assigned_quest.quest_id
  