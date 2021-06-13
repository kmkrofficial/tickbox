from flask import Flask
from flask_restful import Resource, Api

from pipeline import getCosineSimilarityFromOnline, getCosineSimilarityFromDrive

app = Flask(__name__)
api = Api(app)


class TickBoxOnline(Resource):
    def get(self, question, file_name):
        return getCosineSimilarityFromOnline(question, file_name)


class TickBoxDrive(Resource):
    def get(self, question, file_name):
        return getCosineSimilarityFromDrive(question, file_name)


api.add_resource(TickBoxOnline, "/to/<string:question>/<string:file_name>")

api.add_resource(TickBoxDrive, "/td/<string:question>/<string:file_name>")

if __name__ == '__main__':
    app.run(debug=True)
