from flask import Flask, request
from sqlalchemy import Table, Column, Integer, String, MetaData

from src.classes.socialcause import SocialCause
from src.classes.volunteer import Volunteer
from src.db.DBSession import DBSession
from src.db.DBSession import VolunteerDB
from src.db.DBSession import SocialCauseDB


class AtadosAPI(DBSession):
    def __init__(self):

        self.app = Flask(__name__)
        self.app.route('/api/v1/newvolunteer',   methods=['POST'])(self.new_volunteer)
        self.app.route('/api/v1/newsocialcause', methods=['POST'])(self.new_social_cause)
        self.app.route('/api/v1/volunteers',     methods=['GET'])(self.get_volunteers)
        self.app.route('/api/v1/socialcauses',   methods=['GET'])(self.get_social_causes)

        self.volunteers = []
        self.social_causes = []

    def new_volunteer(self):
        data = request.get_json()
        try:
            volunteer = Volunteer(data['name'], data['surname'], data['neighborhood'], data['city'])
            self.volunteers.append(volunteer)
            volunteer_db = self.create_volunteer_db(volunteer)
            self.session.add(volunteer_db)
            self.session.commit()
            return('voluntario salvo')
        except Exception as e:
            print('*Error*: formato do json body pode nao estar correto! Except: ' + str(e))
            return ('400 Bad format body; Except: ' + str(e))
    
    def new_social_cause(self):
        data = request.get_json()
        try:
            social_cause = SocialCause(data['name'], data['institution_name'], data['adress'], data['description'])
            self.social_causes.append(social_cause)
            social_cause_db = self.create_social_cause_db(social_cause)
            self.session.add(social_cause_db)
            self.session.commit()
            return('acao social salva')
        except Exception as e:
            print('*Error*: formato do json body pode nao estar correto! Except: ' + str(e))
            return ('400 Bad format body; Except: ' + str(e))
    
    def get_volunteers(self):
        metadata = MetaData()
        volunteers = Table('volunteer_db', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('surname', String),
                    Column('neighborhood', String),
                    Column('city', String),
        )
        
        query = self.session.query(volunteers)
        results = []
        for row in query:
            results.append({
                'id': row[0],
                'name': row[1],
                'surname': row[2],
                'neighborhood': row[3],
                'city': row[4],
            })
        return (results)
    
    def get_social_causes(self):
        metadata = MetaData()
        social_causes = Table('social_cause_db', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('institution_name', String),
                    Column('adress', String),
                    Column('description', String),
        )
        
        query = self.session.query(social_causes)
        results = []
        for row in query:
            results.append({
                'id': row[0],
                'name': row[1],
                'institution_name': row[2],
                'adress': row[3],
                'description': row[4],
            })
        return (results)
    
    def create_volunteer_db(self, volunteer: Volunteer):
        return(VolunteerDB(name=volunteer.name, surname=volunteer.surname, neighborhood=volunteer.neighborhood, city=volunteer.city))
        
    def create_social_cause_db(self, social_cause: SocialCause):
        return(SocialCauseDB(name=social_cause.name, institution_name=social_cause.institution_name, adress=social_cause.adress, description=social_cause.description))