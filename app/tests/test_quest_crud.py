import pytest

from sqlalchemy.orm import Session

from models import Quest
from crud.quests import QuestCrud

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
def quest(session: Session) -> Quest:
  quest = Quest(title='First Quest', description='Your journey belongs here', reward=100)
  session.add(quest)
  session.flush()
  return quest

@pytest.fixture
def crud(session: Session) -> QuestCrud:
  return QuestCrud(session)

def test_quest_creation(crud: QuestCrud):
  quest = crud.add(title='First Quest', description='Your journey belongs here', reward=100)
  
  assert quest.id is not None

def test_get_quest(crud: QuestCrud, quest: Quest):
  found_quest = crud.get(id=quest.id)

  assert found_quest.id == quest.id
  assert found_quest.title == 'First Quest'
  assert found_quest.description == 'Your journey belongs here'
  assert found_quest.reward == 100

def test_list_quests(crud: QuestCrud, quest: Quest):
  quests = crud.list()

  assert quest in quests

def test_update_quest(crud: QuestCrud, quest: Quest):
  updated_quest = crud.update(id=quest.id, title='Updated Quest')

  assert updated_quest.title == 'Updated Quest'

def test_delete_quest(crud: QuestCrud, quest: Quest):
  crud.delete(id=quest.id)
  deleted_quest = crud.get(id=quest.id)

  assert deleted_quest is None