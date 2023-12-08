import logging

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from utils import sum_sales_by_column

logging.basicConfig(level=logging.INFO)

sales_period_bp = Blueprint('sales_period_bp', __name__)


@sales_period_bp.route('/employee', methods=['GET'])
@jwt_required()
def period_employee():
    """
    Endpoint to get the sum of sales for an employee within a given date range.
    Returns the employee, start date, end date, and total sales amount.
    """
    key_employee = request.args.get('KeyEmployee')
    start_date = request.args.get('StartDate')
    end_date = request.args.get('EndDate')
    column = 'KeyEmployee'

    if not key_employee or not start_date or not end_date:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sum = sum_sales_by_column(column, key_employee, start_date, end_date)

    return jsonify({
        'Key_employee': key_employee,
        'Start_date': start_date,
        'End_date': end_date,
        'Total_sales': total_sum
    })


@sales_period_bp.route('/product', methods=['GET'])
@jwt_required()
def period_product():
    """
    Endpoint to get the sum of sales for a product within a given date range.
    Returns the product, start date, end date, and total sales amount.
    """
    key_product = request.args.get('KeyProduct')
    start_date = request.args.get('StartDate')
    end_date = request.args.get('EndDate')
    column = 'KeyProduct'

    if not key_product or not start_date or not end_date:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sum = sum_sales_by_column(column, key_product, start_date, end_date)

    return jsonify({
        'Key_product': key_product,
        'Start_date': start_date,
        'End_date': end_date,
        'Total_sales': total_sum
    })


@sales_period_bp.route('/store', methods=['GET'])
@jwt_required()
def period_store():
    """
    Endpoint to get the sum of sales for a store within a given date range.
    Returns the store, start date, end date, and total sales amount.
    """
    key_store = request.args.get('KeyStore')
    start_date = request.args.get('StartDate')
    end_date = request.args.get('EndDate')
    column = 'KeyStore'

    if not key_store or not start_date or not end_date:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sum = sum_sales_by_column(column, key_store, start_date, end_date)

    return jsonify({
        'Key_store': key_store,
        'Start_sate': start_date,
        'End_sate': end_date,
        'Total_sales': total_sum
    })