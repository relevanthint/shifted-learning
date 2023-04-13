from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

base_wording_model = Table("base_wording", meta, 
              Column("id", Integer, primary_key=True, autoincrement=True),
              Column("base_wording", String(255)), 
              Column("theme", String(255)), 
              Column("tone", String(255)), 
              Column("length", String(255)),
              Column("learning_objective", String(255)))

shifted_wording_model = Table("shifted_wording", meta, 
              Column("id", Integer, primary_key=True, autoincrement=True),
              Column("base_wording_id", Integer), 
              Column("shifted_wording", String(255)))


meta.create_all(engine)