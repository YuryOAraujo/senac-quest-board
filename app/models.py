from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class Character(Base):
  __tablename__ = 'characters'

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(80))
  level: Mapped[int]
  gold: Mapped[int]

  def __repr__(self):
    return f'Character(id={self.id}, name={self.name}, level={self.level}, gold={self.gold})'

class Quest(Base):
  __tablename__ = 'quests'

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]
  description: Mapped[str]
  reward: Mapped[int]

  def __repr__(self):
    return f'Quest(id={self.id}, title={self.title}, reward={self.reward}, description={self.description})'