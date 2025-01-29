from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    user_id = len(users) + 1
    users[user_id] = user_data
    return jsonify({"message": "User registered", "user_id": user_id})

@app.route('/login', methods=['POST'])
def login():
    credentials = request.json
    for user_id, user in users.items():
        if user['email'] == credentials['email'] and user['password'] == credentials['password']:
            return jsonify({"message": "Login successful", "user_id": user_id})
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)