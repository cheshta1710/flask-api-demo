from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Pong!'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

