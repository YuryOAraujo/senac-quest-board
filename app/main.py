from crud import Crud
from models import Base
from db import engine, SessionLocal

def app():
  Base.metadata.create_all(engine)

  with SessionLocal() as session:
    crud = Crud(session)
    character = crud.add(name='Grimma', level=1, gold=100)

    print('ADD', character)
    print('GET', crud.get(name='Grimma'))
    print('UPDATE', crud.update(id=character.id, name='Lah Ghar', level=2, gold=50))
    print('LIST', crud.list())
    print('DELETE', crud.delete(id = character.id))

if __name__ == '__main__':
  app()