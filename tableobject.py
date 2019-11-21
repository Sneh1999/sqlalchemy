from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

meta = MetaData()
t = Table('ex_table', meta,
          Column('id', Integer, primary_key=True),
          Column('key', String),
          Column('val', Integer))
# Get Table Name
print(t.name)

# Get Columns
print(t.columns.keys())

# Get Column
c = t.c.key
print(c.name)
# Or
c = t.columns.key
print(c.name)

