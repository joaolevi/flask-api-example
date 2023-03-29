from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class VolunteerDB(Base):
    __tablename__ = 'volunteer_db'

    id           = Column(Integer, primary_key=True)
    name         = Column(String(50))
    surname      = Column(String(50))
    neighborhood = Column(String(50))
    city         = Column(String(50))

class SocialCauseDB(Base):
    __tablename__ = 'social_cause_db'

    id               = Column(Integer, primary_key=True)
    name             = Column(String(50))
    institution_name = Column(String(50))
    adress           = Column(String(120))
    description      = Column(String(200))

class DBSession():
    def __init__(self):
        self.session = None
        self.engine = None
    
    def start_db_session(self):
        self.engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.create_all(self.engine)

    def save_to_db(self, data):
        print('Entrou aqui nessa merda')
        if (self.session.connection()):
            self.session.add(data)
            self.session.commit()
        else:
            self.start_db_session()