import pytest

from sqlalchemy.orm import Session

from models import Quest
from crud.quests import QuestCrud

@pytest.fixture
def session():
  pass

@pytest.fixture
def quest(session: Session) -> Quest:
  pass

@pytest.fixture
def crud(session: Session) -> QuestCrud:
  pass

def test_quest_creation(crud: QuestCrud):
  pass

def test_get_quest(crud: QuestCrud):
  pass

def test_list_quests(crud: QuestCrud, quest: Quest):
  pass

def test_update_quest(crud: QuestCrud, quest: Quest):
  pass

def test_delete_quest(crud: QuestCrud, quest: Quest):
  pass