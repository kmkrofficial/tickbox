from flask import Flask, jsonify
from flask_restful import Resource, Api

from pipeline import getCosineSimilarityFromOnline, getCosineSimilarityFromDrive

app = Flask(__name__)
api = Api(app)


class TickBoxOnline(Resource):
    def post(self, question, file_name):
        print("Success")
        return jsonify(getCosineSimilarityFromOnline(question, file_name))


class TickBoxDrive(Resource):
    def post(self, question, file_name):
        return jsonify(getCosineSimilarityFromDrive(question, file_name))


api.add_resource(TickBoxOnline, "/to/<string:question>/<string:file_name>")
api.add_resource(TickBoxDrive, "/td/<string:question>/<string:file_name>")

if __name__ == '__main__':
    app.run(debug=True)
