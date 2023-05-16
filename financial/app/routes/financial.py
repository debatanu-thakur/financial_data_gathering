from flask import Blueprint, request
from flask.json import jsonify
from app.services import FinancialService
from app.utils import ErrorHandlerFactory

financial = Blueprint('financial', __name__)  # pylint: disable=C0103
FIN_SERVICE = FinancialService()

@financial.route('search', methods=['GET'])
def get_financial_data():
    try:
        query_parameters = dict(request.args)
        resp = FIN_SERVICE.get_search_results(query_parameters)
        return jsonify(resp)
    except Exception as error:
        error_handler = ErrorHandlerFactory.get_error_handler(error)
        return error_handler.handle_error()

