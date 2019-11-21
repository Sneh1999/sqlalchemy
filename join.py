from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select


db_uri = 'sqlite:///db.sqlite'

engine = create_engine(db_uri)

meta = MetaData(engine).reflect()

email_t = Table('email_addr',meta,
                Column("id",Integer, primary_key=True
                Column('email',String),
                Column('name', String)))

meta.create_all()


user_t = meta.tables['user']


conn = engine.connect()

conn.excecute(email_t.insert(),[
    {'email' : 'vsdusd@gmail.com', 'name': 'Hi'},
    {'email': 'yo@test', 'name': 'Hello'}
])

join_obj = user_t.join(email_t, email_t.c.name == user_t.c.l.name)

sel_st = select(
    [
        user_t.c.l_name, email_t.c.email
    ]
).select_from(join_obj)

for _row in res:
    print(_row)

