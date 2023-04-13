from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:mysql-juanm@localhost:3306/shifteddb")

meta = MetaData()

conn = engine.connect()