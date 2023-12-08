import logging

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from utils import sum_and_average_sales_by_column

logging.basicConfig(level=logging.INFO)

total_sales_bp = Blueprint('total_sales_bp', __name__)


@total_sales_bp.route('/employee', methods=['GET'])
@jwt_required()
def total_employee():
    """
    Endpoint to get the sum and average of sales for an employee.
    Returns the employee, total and average.
    """
    key_employee = request.args.get('KeyEmployee')
    column = 'KeyEmployee'

    if not key_employee:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sales, average_sales = sum_and_average_sales_by_column(column, key_employee)

    return jsonify({
        'Key_employee': key_employee,
        'Total_sales': total_sales,
        'Average_sales': average_sales
    })


@total_sales_bp.route('/product', methods=['GET'])
@jwt_required()
def total_product():
    """
    Endpoint to get the sum and average of sales for a product.
    Returns the product, total and average.
    """
    key_product = request.args.get('KeyProduct')
    column = 'KeyProduct'

    if not key_product:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sales, average_sales = sum_and_average_sales_by_column(column, key_product)

    return jsonify({
        'Key_Product': key_product,
        'Total_sales': total_sales,
        'Average_sales': average_sales
    })


@total_sales_bp.route('/store', methods=['GET'])
@jwt_required()
def total_store():
    """
    Endpoint to get the sum and average of sales for a store.
    Returns the store, total and average.
    """
    key_store = request.args.get('KeyStore')
    column = 'KeyStore'

    if not key_store:
        logging.warning("Missing parameters for calculating sales.")
        return jsonify({'message': 'Missing parameters.'}), 400

    total_sales, average_sales = sum_and_average_sales_by_column(column, key_store)

    return jsonify({
        'Key_Product': key_store,
        'Total_sales': total_sales,
        'Average_sales': average_sales
    })