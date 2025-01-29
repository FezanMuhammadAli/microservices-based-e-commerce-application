from flask import Flask, jsonify, request

app = Flask(__name__)

carts = {}

@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts.get(user_id, [])
    return jsonify(cart)

@app.route('/cart/<int:user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    item = request.json
    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append(item)
    return jsonify({"message": "Item added to cart"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)