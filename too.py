from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import or_

meta = MetaData()

table = Table('example', meta , 
          Column('id', Integer, primary_key=True),
          Column('l_name', String),
          Column('f_name', String))

print(repr(table.c.l_name == 'ed'))

print(str(table.c.l_name == 'ed'))

print(repr(table.c.f_name != 'ed'))

print(repr(table.c.id > 3))

print((table.c.id > 5) | (table.c.id < 2))

print(or_(table.c.id > 5 , table.c.id < 2))

print(table.c.l_name == None)

print(table.c.l_name.is_(None))

print(table.c.l_name + "some name")

