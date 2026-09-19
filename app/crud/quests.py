from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Quest

class QuestCrud():
  def __init__(self, session: Session):
    self.session = session

  def add(self, **kwargs) -> Quest: 
    quest = Quest(**kwargs)
    self.session.add(quest)
    return quest

  def list(self) -> List[Quest]:
    statement = select(Quest)
    return self.session.scalars(statement).all()

  def get(self, **kwargs) -> Quest | None:
    statement = select(Quest).filter_by(**kwargs)
    return self.session.scalars(statement).first()

  def delete(self, **kwargs) -> Quest | None:
    quest = self.get(**kwargs)

    if quest:
      self.session.delete(quest)

    return quest

  def update(self, **kwargs) -> Quest | None:
    id = kwargs.get('id')

    quest = self.get(id=id)

    if quest is None:
      return None

    allowed_fields = {'title', 'description', 'reward'}

    for key, value in kwargs.items():
      if key in allowed_fields:
        setattr(quest, key, value)

    return quest