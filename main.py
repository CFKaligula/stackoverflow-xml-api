from flask import Flask
from flask_restful import Api

from resources.so_xml_analyser import StackOverflowXMLAnalyser

app = Flask(__name__)
api = Api(app)
api.add_resource(StackOverflowXMLAnalyser, '/analyze')

if __name__ == '__main__':
    app.run(debug=True)
