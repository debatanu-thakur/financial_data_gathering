from flask import Blueprint, request
from flask.json import jsonify


statistics = Blueprint('statistics', __name__)  # pylint: disable=C0103

@statistics.route('get', methods=['GET'])
def get_statistics():
    return "I am stats"