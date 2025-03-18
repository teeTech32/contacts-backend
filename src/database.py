from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://contactpsql_user:pZrSTrbqvoAKe774swJQsJMISLl3bqXD@dpg-cvcujrqj1k6c73dkj480-a/contactpsql'
            

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


