import json
import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from dotenv import load_dotenv
from wsgiref.simple_server import make_server

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/v1/echo', methods=['POST'])
def check_comprehend():
    if request.data is not None:
        payload = request.json
        data = payload['data']
        document_id = data['document_id']
        response = {'message': 'success', 'data': {'document_id': document_id}}
        return jsonify(response), 200
    else:
        response = {'message': 'error'}
        return jsonify(response), 500


@app.route('/v1/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'message': 'success'}), 200


if __name__ == '__main__':
    server = make_server('0.0.0.0', 3000, app)
    server.serve_forever()
