from sqlalchemy import create_engine

db_uri = "sqlite:///db.sqlite"
engine = create_engine(db_uri)


engine.execute('CREATE TABLE "EX2" ( '
                'id INTEGER NOT NULL,'
                'name VARCHAR, '
                'PRIMARY KEY(id));')


engine.execute('INSERT INTO "EX2" '
               '(id, name)'
               'VALUES (2,"raw")')


result = engine.execute('SELECT * FROM '
                        '"EX2"')

for r in result:
    print(r)


engine.execute('DELETE from "EX2" where id=2;')


print(result.fetchall())