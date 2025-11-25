from flask import Blueprint, jsonify
from utils.order_manager import OrderManager

api_bp = Blueprint('api', __name__, url_prefix='/api')
order_mgr = OrderManager()

@api_bp.route('/order/<int:order_id>/status')
def order_status(order_id):
    details = order_mgr.get_order_details(order_id)
    if details:
        return jsonify({'status': details['order']['status']})
    return jsonify({'error': 'Order not found'}), 404
