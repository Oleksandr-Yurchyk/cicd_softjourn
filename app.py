from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hi there! This app has two endpoints: '
            '1. /api/add - to add 2 numbers; '
            '2. /api/multiply - to multiply 2 numbers.')


@app.route('/api/add', methods=['POST'])
def add_two_numbers():
    data = request.get_json()
    result = data.get('num1', 0) + data.get('num2', 0)

    return jsonify({'result': result})


@app.route('/api/multiply', methods=['POST'])
def multiply_two_numbers():
    data = request.get_json()
    result = data.get('num1', 0) * data.get('num2', 0)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
