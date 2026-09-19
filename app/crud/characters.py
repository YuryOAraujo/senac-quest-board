from typing import List

from models import Character
from sqlalchemy.orm import Session
from sqlalchemy import select

class CharacterCrud():
  def __init__(self, session: Session):
    self.session = session

  def add(self, **kwargs) -> Character:
    character = Character(**kwargs)
    self.session.add(character)
    return character

  def update(self, **kwargs) -> Character | None:
    id = kwargs.get('id')

    character = self.get(id=id)

    if character is None:
      return None

    allowed_fields = {'name', 'level', 'gold'}

    for key, value in kwargs.items():
      if key in allowed_fields:
        setattr(character, key, value)

    return character

  def delete(self, **kwargs) -> Character | None:
    character = self.get(**kwargs)

    if character:
      self.session.delete(character)

    return character

  def list(self) -> List[Character]:
    statement = select(Character)    
    return self.session.scalars(statement).all()

  def get(self, **kwargs) -> Character | None:
    statement = select(Character).filter_by(**kwargs)
    return self.session.scalars(statement).first()