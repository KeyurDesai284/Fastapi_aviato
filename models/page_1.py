from sqlalchemy import Boolean, Integer, String, Column
from config.db import Base

class Page1User(Base):
    __tablename__ = 'p_1_user'
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)