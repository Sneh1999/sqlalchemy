from sqlalchemy import create_engine

db_uri = 'sqlite:///db.sqlite'

engine = create_engine(db_uri)


conn = engine.connect()

trans = conn.begin()

conn.execute('INSERT INTO "EX1" (name) VALUES ("HELLO")')

trans.commit()

conn.close()
