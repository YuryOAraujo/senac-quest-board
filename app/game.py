from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Character, Quest, CharacterQuest
from exceptions import QuestAssignmentNotFoundError, QuestAlreadyCompletedError, QuestNotCompleted, RewardAlreadyClaimedError

def complete_quest(session: Session, character_id: int, quest_id: int):
  assigned_quest = session.get(CharacterQuest, (character_id, quest_id))

  if assigned_quest is None:
    raise QuestAssignmentNotFoundError('The quest assignment that you seem to be looking for, could not be found.')

  if assigned_quest.is_completed:
      raise QuestAlreadyCompletedError('This quest has already been completed for this character.')

  assigned_quest.is_completed = True
  _claim_rewards(assigned_quest)

def _claim_rewards(assigned_quest: CharacterQuest):
  if assigned_quest is None:
    raise QuestAssignmentNotFoundError('The quest assignment that you seem to be looking for, could not be found.')

  if not assigned_quest.is_completed:
    raise QuestNotCompleted('You are not able to claim rewards, of an uncompleted quest.')

  if assigned_quest.is_reward_claimed:
    raise RewardAlreadyClaimedError('This reward already has been claimed by this character.')

  character = assigned_quest.character
  quest = assigned_quest.quest

  character.gold += quest.reward
  assigned_quest.is_reward_claimed = True

def unassign_quest(session: Session, character_id: int, quest_id: int) -> CharacterQuest:
  # assigned_quest = session.scalars(select(CharacterQuest).where(CharacterQuest.character_id == character_id, CharacterQuest.quest_id == quest_id)).first()
  assigned_quest = session.get(CharacterQuest, (character_id, quest_id))

  if assigned_quest is None:
    raise QuestAssignmentNotFoundError('The quest assignment that you seem to be looking for, could not be found.')

  if assigned_quest.is_completed:
    raise QuestAlreadyCompletedError('This quest has already been completed for this character, therefore it cannot be unassigned.')
  
  session.delete(assigned_quest)