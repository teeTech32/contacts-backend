from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactsdb_ph8z_user:GtxFB4b2Hl6zNH4S6l2qbk2fVm2Yhzru@dpg-ct6ao8pu0jms73957deg-a/contactsdb_ph8z'



engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


