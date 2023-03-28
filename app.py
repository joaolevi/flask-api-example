from src.api.atadosapi import AtadosAPI

if __name__ == '__main__':
    app = AtadosAPI().app
    app.run()