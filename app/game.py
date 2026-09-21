from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Character, Quest, CharacterQuest

def complete_quest(session: Session, character_id: int, quest_id: int):
  pass

def claim_rewards(session: Session, character_id: int, quest_id: int):
  pass

def unassign_quest(session: Session, character_id: int, quest_id: int) -> CharacterQuest | None:
  assigned_quest = session.scalars(select(CharacterQuest).where(CharacterQuest.character_id == character_id, CharacterQuest.quest_id == quest_id)).first()

  if assigned_quest:
    session.delete(assigned_quest)

  return assigned_quest