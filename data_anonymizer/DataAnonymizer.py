from flask import Flask
from .informationgenerator import InformationGenerator

def realmain():
    app = Flask(__name__)
    infogen = InformationGenerator()

    @app.route('/')
    def root():
        return infogen.phonenumber()

    app.run('127.0.0.1', 8000)
