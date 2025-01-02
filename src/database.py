from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactsdb_fhdr_user:ZODM5oU1BMxo6bFu9R6yOZtzICFYtsvz@dpg-ctr8b7dsvqrc73d3e9n0-a/contactsdb_fhdr'



engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


