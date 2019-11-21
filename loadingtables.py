from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

metadata = MetaData()

print(metadata.tables)

metadata.reflect(bind=engine)

print(metadata.tables)

ex_table = metadata.tables['Example']

print('ex tables', ex_table)



