from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactsdb_kq9t_user:tHoqR5wrUj5yvzLxnuPBfUHY2SnTrPYF@dpg-cuflgvdds78s73fm9ld0-a/contactsdb_kq9t
'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


