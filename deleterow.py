from sqlalchemy import create_engine
from sqlalchemy import MetaData


db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

conn = engine.connect()

meta = MetaData(engine).reflect()
user_t = meta.tables['user']


sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res:
    print(_row)


del_st = user_t.delete().where(
    user_t.c.l_name == 'Hello'
)

res = conn.execute(del_st)

