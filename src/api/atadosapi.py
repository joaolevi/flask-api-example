from flask import Flask, request
from json import dumps
from sqlalchemy.orm import declarative_base

from src.classes.socialcause import SocialCause
from src.classes.volunteer import Volunteer
from src.db.DBSession import DBSession, VolunteerDB, SocialCauseDB

class AtadosAPI():
    def __init__(self):

        self.app = Flask(__name__)
        self.app.route('/api/v1/newvolunteer',   methods=['POST'])(self.new_volunteer)
        self.app.route('/api/v1/newsocialcause', methods=['POST'])(self.new_social_cause)
        self.app.route('/api/v1/volunteers',     methods=['GET'])(self.get_volunteers)
        self.app.route('/api/v1/socialcauses',   methods=['GET'])(self.get_social_causes)

        self.volunteers = []
        self.social_causes = []
        self.db = None

    def new_volunteer(self):
        data = request.get_json()
        try:
            volunteer = Volunteer(data['name'], data['surname'], data['neighborhood'], data['city'])
            self.volunteers.append(volunteer)
            volunteer_db = self.create_volunteer_db(volunteer)
            self.db.save_to_db(volunteer_db)
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
            self.db.save_to_db(social_cause_db)
            return('acao social salva')
        except Exception as e:
            print('*Error*: formato do json body pode nao estar correto! Except: ' + str(e))
            return ('400 Bad format body; Except: ' + str(e))
    
    def get_volunteers(self):
        json_volunteers = dumps([v.__dict__ for v in self.volunteers], ensure_ascii=False)
        return (json_volunteers)
    
    def get_social_causes(self):
        json_social_causes = dumps([v.__dict__ for v in self.social_causes], ensure_ascii=False)
        return (json_social_causes)
    
    def create_volunteer_db(self, volunteer: Volunteer):
        return(VolunteerDB(name=volunteer.name, surname=volunteer.surname, neighborhood=volunteer.neighborhood, city=volunteer.city))
        
    def create_social_cause_db(self, social_cause: SocialCause):
        return(SocialCauseDB(name=social_cause.name, institution_name=social_cause.institution_name, adress=social_cause.adress, description=social_cause.description))

    def connect_db_session(self):
        self.db = DBSession()
        self.db.start_db_session()
