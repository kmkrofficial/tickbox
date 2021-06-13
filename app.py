from flask import Flask
from flask_restful import Resource, Api

from pipeline import getCosineSimilarity

app = Flask(__name__)
api = Api(app)


class TickBox(Resource):
    def get(self, question, file_name):
        return getCosineSimilarity(question, file_name)


api.add_resource(TickBox, "/tickbox/<string:question>/<string:file_name>")

if __name__ == '__main__':
    app.run(debug=True)
