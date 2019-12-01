import io
import os

from flask import Flask, request, Response, jsonify
import detecttext

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/receipt', methods=['POST'])
def get_total():
    data = request.data

    # Hardcode if neccessary
    # receipt_path = os.path.abspath('/bin/receipt3.jpg')
    #
    # # Loads the image into memory
    # with io.open(receipt_path, 'rb') as image_file:
    #     data = image_file.read()

    try:
        detecttext.checkReceipt(data)
        json_result = detecttext.get_total(data)
        return jsonify(total=str(json_result), response=200)
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run()
    detecttext.run_quickstart()
