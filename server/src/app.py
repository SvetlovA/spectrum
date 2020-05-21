from flask import Flask, render_template, jsonify, request
from algorithms.implementation.haar_algorithm import HaarAlgotithm


APP = Flask('spectrum', template_folder='src/templates')

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/filter', methods=['POST'])
def filter_signal() -> list:
    input_request = request.json

    algorithm = HaarAlgotithm()
    result_signal = algorithm.filter_signal(
        input_request['input_signal'], input_request['threshold'])

    return jsonify(result_signal)

if __name__ == "__main__":
    APP.run()
