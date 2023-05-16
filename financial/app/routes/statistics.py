from flask import Blueprint, request
from flask.json import jsonify
from app.services import StatisticService
from app.utils import ErrorHandlerFactory


statistics = Blueprint('statistics', __name__)  # pylint: disable=C0103

STAT_SERVICE = StatisticService()
@statistics.route('get', methods=['GET'])
def get_statistics():
    try:
        query_parameters = dict(request.args)
        resp = STAT_SERVICE.get_daily_average_results(query_parameters)
        return jsonify(resp)
    except Exception as error:
        error_handler = ErrorHandlerFactory.get_error_handler(error)
        return error_handler.handle_error()