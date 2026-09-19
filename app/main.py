from crud.quests import QuestCrud
from crud.characters import CharacterCrud
from models import Base
from db import engine, SessionLocal

def app():
  Base.metadata.create_all(engine)

  with SessionLocal.begin() as session:
    crud = CharacterCrud(session)
    character = crud.add(name='Grimma', level=1, gold=100)

    print('ADD', character)
    print('GET', crud.get(name='Grimma'))
    print('UPDATE', crud.update(id=character.id, name='Lah Ghar', level=2, gold=50))
    print('LIST', crud.list())
    print('DELETE', crud.delete(id = character.id))

    crud = QuestCrud(session)

    quest = crud.add(title='Quest 1', description='Description', reward=100)
    print('ADD', quest)
    print('GET', crud.get(title='Quest 1'))
    print('UPDATE', crud.update(id=quest.id, title='New Title', description='New Description', reward=200))
    print('LIST', crud.list())
    print('DELETE', crud.delete(id=quest.id))

if __name__ == '__main__':
  app()