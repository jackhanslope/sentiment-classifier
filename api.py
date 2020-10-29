from model import NLPModel

from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

model = NLPModel()
model.load_vectorizer()
model.load_clf()

parser = reqparse.RequestParser()
parser.add_argument('query')

# PredictSentiment
# Predicts the sentiment of an input review
class PredictSentiment(Resource):
    def get(self):
        args = parser.parse_args()
        user_query = args['query']

        prediction = model.predict([user_query])
        text = 'Positive' if prediction == [1] else 'Negative'

        output = {'prediction': text}

        return output

api.add_resource(PredictSentiment, '/')

if __name__ == '__main__':
    app.run(debug=True)
