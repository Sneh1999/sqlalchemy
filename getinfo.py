from sqlalchemy import create_engine
from sqlalchemy import inspect

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)


inspector = inspect(engine)

print(inspector.get_table_names())

print(inspector.get_columns('EX1'))