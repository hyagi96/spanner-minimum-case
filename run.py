#!/usr/bin/env python3
import datetime
import os
import uuid

from dotenv import load_dotenv
from sqlalchemy import Column, Text, TIMESTAMP, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# load environment from ./.env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'), verbose=True)

PROJECT_ID = os.getenv('PROJECT_ID')
INSTANCE_ID = os.getenv('INSTANCE_ID')
DATABASE_ID = os.getenv('DATABASE_ID')
SQLALCHEMY_DATABASE_URL = (f'spanner:///projects/{PROJECT_ID}/instances/'
                           f'{INSTANCE_ID}/databases/{DATABASE_ID}')

# Schema
Base = declarative_base()

class Table(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.uuid:
            self.uuid = str(uuid.uuid4())

    __tablename__ = 'testtable'

    uuid = Column(VARCHAR(36), primary_key=True)
    timestamp = Column(TIMESTAMP)

# engine, session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
maker = sessionmaker(bind=engine)
session = maker()

# Apply schema using the engine
Base.metadata.create_all(engine)

# Add a column or Update the existing one
column = session.query(Table).first()
if column:
    column.timestamp = datetime.datetime.now()
else:
    column = Table(timestamp=datetime.datetime.now())
print(column.timestamp)

session.add(column)
session.commit()
session.close()
