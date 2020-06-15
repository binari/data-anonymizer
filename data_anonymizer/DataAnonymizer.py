from flask import Flask, render_template, url_for
from .informationgenerator import InformationGenerator

def realmain():
    app = Flask(__name__)
    infogen = InformationGenerator()

    @app.route('/')
    def root():
        return infogen.phonenumber()

    @app.route('/test')
    def test():
        return render_template('test.html')

    app.run('127.0.0.1', 8000)
