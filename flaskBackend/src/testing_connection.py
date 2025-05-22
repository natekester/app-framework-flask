from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres@postgres:5432/base_db")
engine.connect()
print('done')
