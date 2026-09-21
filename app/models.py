from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
  pass

class Character(Base):
  __tablename__ = 'characters'

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(80))
  level: Mapped[int]
  gold: Mapped[int]

  assigned_quests: Mapped[List['CharacterQuest']] = relationship(back_populates='character')

  def __repr__(self):
    return f'Character(id={self.id}, name={self.name}, level={self.level}, gold={self.gold})'

class Quest(Base):
  __tablename__ = 'quests'

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]
  description: Mapped[str]
  reward: Mapped[int]

  assigned_characters: Mapped[List['CharacterQuest']] = relationship(back_populates='quest')

  def __repr__(self):
    return f'Quest(id={self.id}, title={self.title}, reward={self.reward}, description={self.description})'

class CharacterQuest(Base):
  __tablename__ = 'character_quests'

  character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'), primary_key=True)
  quest_id: Mapped[int] = mapped_column(ForeignKey('quests.id'), primary_key=True)
  is_completed: Mapped[bool] = mapped_column(default=False)
  is_reward_claimed: Mapped[bool] = mapped_column(default=False)

  character: Mapped[List['Character']] = relationship(back_populates='assigned_quests')
  quest: Mapped[List['Quest']] = relationship(back_populates='assigned_characters')