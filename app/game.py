from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Character, Quest, CharacterQuest
from exceptions import QuestAssignmentNotFoundError, QuestAlreadyCompletedError

def complete_quest(session: Session, character_id: int, quest_id: int):
  pass

def claim_rewards(session: Session, character_id: int, quest_id: int):
  pass

def unassign_quest(session: Session, character_id: int, quest_id: int) -> CharacterQuest:
  assigned_quest = session.scalars(select(CharacterQuest).where(CharacterQuest.character_id == character_id, CharacterQuest.quest_id == quest_id)).first()

  if assigned_quest is None:
    raise QuestAssignmentNotFoundError('The quest that you seem to be looking for, could not be found.')

  if assigned_quest.is_completed:
    raise QuestAlreadyCompletedError('This quest has already been completed for this character, therefore it cannot be unassigned.')
  
  session.delete(assigned_quest)