from src.api.atadosapi import AtadosAPI
from flask import current_app

if __name__ == '__main__':
    atados = AtadosAPI()
    atados.start_db_session()
    atados.app.run(host='0.0.0.0',debug=False,port='5000')