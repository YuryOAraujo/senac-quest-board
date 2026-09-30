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

def test_get_quest(crud: QuestCrud):
  pass

def test_list_quests(crud: QuestCrud, quest: Quest):
  pass

def test_update_quest(crud: QuestCrud, quest: Quest):
  pass

def test_delete_quest(crud: QuestCrud, quest: Quest):
  pass