from sqlalchemy import create_engine
from models import Base


engine = create_engine('sqlite:///library.db')

Base.metadata.create_all(engine)

print("База данных и таблицы успешно созданы!")