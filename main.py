import os

from flask import Flask, request, Response, jsonify
import detecttext

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/receipt', methods=['PUT'])
def get_total():
    data = request.get_json()
    try:
        json_result = detecttext.detect_text(os.path.abspath('bin/receipt1.jpg'))
        return jsonify(total=str(json_result), response=200)
    except Exception as e:
        return jsonify(e, response=400)

if __name__ == '__main__':
    app.run()
