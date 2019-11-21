from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)


meta = MetaData(engine)

table = Table('user', meta,
              Column('id',Integer, primary_key=True),
              Column('l_name',String),
              Column('f_name',String))

meta.create_all()

ins = table.insert().values(
    l_name='Hello',
    f_name='World'
)

conn = engine.connect()
conn.execute(ins)

conn.execute(table.insert(), [
    {'l_name': 'Hi', 'f_name': 'bob'},
    {'l_name':'yo','f_name':'alice'}
])