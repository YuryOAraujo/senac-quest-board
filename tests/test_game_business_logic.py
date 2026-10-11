import pytest

from app.crud.characters import CharacterCrud
from app.crud.quests import QuestCrud
from app.models import Character, Quest, CharacterQuest
from app.db import SessionLocal
from sqlalchemy.orm import Session
import app.game as game
from app.exceptions import QuestAlreadyCompletedError, QuestAssignmentNotFoundError

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

def test_complete_quest(session: Session, character: Character, quest: Quest, assigned_quest: CharacterQuest):
  current_gold = character.gold
  game.complete_quest(session, character.id, quest.id)

  completed_quest = session.get(CharacterQuest, (character.id, quest.id))

  assert completed_quest is assigned_quest
  assert completed_quest.is_completed
  assert completed_quest.is_reward_claimed
  assert (current_gold + quest.reward) == character.gold

def test_quest_already_completed(session: Session, assigned_quest: CharacterQuest):
  with pytest.raises(QuestAlreadyCompletedError):
    assigned_quest.is_completed = True
    game.complete_quest(session, assigned_quest.character.id, assigned_quest.quest.id)

def test_quest_assignment_not_found(session: Session, character: Character, quest: Quest):
  with pytest.raises(QuestAssignmentNotFoundError):
    game.complete_quest(session, character.id, quest.id)
  

def test_unassign_quest(session: Session, character: Character, quest: Quest, assigned_quest):
  game.unassign_quest(session, character.id, quest.id)
  session.flush()
  deleted_quest_assignment = session.get(CharacterQuest, (character.id, quest.id))

  assert deleted_quest_assignment is None 

def test_cannot_unassign_quest_already_completed(session: Session, assigned_quest: CharacterQuest):
  with pytest.raises(QuestAlreadyCompletedError):
    assigned_quest.is_completed = True
    game.unassign_quest(session, assigned_quest.character.id, assigned_quest.quest.id)