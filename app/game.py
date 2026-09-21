from sqlalchemy.orm import Session

from app.models import Character, Quest

def complete_quest(session: Session, character: Character, quest: Quest):
  pass

def claim_rewards(session: Session, character: Character, quest: Quest):
  pass

def unassign_quest(session: Session, character: Character, quest: Quest):
  pass