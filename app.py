from src.api.atadosapi import AtadosAPI

if __name__ == '__main__':
    app = AtadosAPI().app
    app.run(host='0.0.0.0',debug=False,port='5000')
