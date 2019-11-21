from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer,String

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

metadata = MetaData(engine)

table = Table('Example',metadata, 
                Column('id',Integer, primary_key=True),
                Column('name', String))

metadata.create_all()

for t in metadata.tables:
    print("Tables", t)