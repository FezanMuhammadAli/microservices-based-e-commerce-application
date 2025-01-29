from flask import Flask, jsonify, request

app = Flask(__name__)

orders = {}

@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    order_id = len(orders) + 1
    orders[order_id] = order_data
    return jsonify({"message": "Order created", "order_id": order_id})

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    return jsonify(order) if order else ("Order not found", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)