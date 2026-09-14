from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class Character(Base):
  __tablename__ = 'characters'

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  level: Mapped[int]
  gold: Mapped[int]