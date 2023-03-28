from src.api.atadosapi import AtadosAPI

if __name__ == '__main__':
    atados = AtadosAPI()
    atados.connect_db_session()
    atados.app.run(host='0.0.0.0',debug=False,port='5000')