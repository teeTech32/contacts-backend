from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://fastapi:csHW3ntrDp6prLRkic3bOkjqGogtXTAn@dpg-csh2go8gph6c73bv0t30-a/contactapplication'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


