from config import client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
from importlib.machinery import SourceFileLoader

helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

db = client.restfulapi
collection = db.users

@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v5.0',
        'status': '200',
        'message': 'Welcome'
    }
    res = jsonify(message)
    return res


@app.route("/api/v5/users", methods=['POST'])
def create_user():
    """
        function to create new users.
       """
    try:
        # Create new users
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        record_inserted = collection.insert(body)
        if isinstance(record_inserted, list):
            return jsonify([str(v) for v in record_inserted]), 201
        else:
            return jsonify(str(record_inserted)), 201
    except:
        return "", 500


@app.route("/api/v5/users", methods=['GET'])
def fetch_users():
    """
       Function to fetch the users.
       """
    try:
        query_params = helper_module.parse_query_params(request.query_string)
        if query_params:
            dbquery = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}
            records_fetched = collection.find(dbquery)
            if records_fetched.count() > 0:
                return dumps(records_fetched)
            else:
                return "", 404
        else:
            if collection.find().count() > 0:
                return dumps(collection.find())
            else:
                return jsonify([])
    except:
        return "", 500


@app.route("/api/v5/users/<user_id>", methods=['POST'])
def update_user(user_id):
    """
       Function to update the user.
       """
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        # Updating the user
        records_updated = collection.update_one({"id": int(user_id)}, body)
        if records_updated.modified_count > 0:
            return "", 200
        else:
            return "", 404
    except:
        return "", 500


@app.route("/api/v5/users/<user_id>", methods=['DELETE'])
def remove_user(user_id):
    """
       Function to remove the user.
       """
    try:
        # Delete the user
        delete_user = collection.delete_one({"id": int(user_id)})

        if delete_user.deleted_count > 0 :
            return "", 204
        else:
            return "", 404
    except:
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    message = {
        "err":
            {
                "msg": "Not Found."
            }
    }
    res = jsonify(message)
    res.status_code = 404
    return res
