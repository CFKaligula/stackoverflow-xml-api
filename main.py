from flask import Flask
from flask_restful import Api

from resources.so_xml_analyser import StackOverflowXMLAnalyser

"""
Script to launch the Flask App
"""

app = Flask(__name__)
api = Api(app)
api.add_resource(StackOverflowXMLAnalyser, '/analyse')

if __name__ == '__main__':
    app.run(debug=True)
