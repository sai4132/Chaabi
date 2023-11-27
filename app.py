from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
from search import query  # Importing the query function from search.py

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Welcome(Resource):
    def get(self):
        return 'Welcome to the Vector DB API!'

class SearchVectorDB(Resource):
    def post(self):
        try:
            data = request.get_json()
            search_string = data.get('search_string')
            if not search_string:
                return {"error": "No search string provided."}, 400

            # Call the query function from search.py
            results = query(search_string)
            return {'results': results}

        except Exception as error:
            return {'error': str(error)}, 500

api.add_resource(Welcome, '/')
api.add_resource(SearchVectorDB, '/search')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
