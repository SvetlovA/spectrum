from flask import Flask


APP = Flask('spectrum')

@APP.route('/')
def index() -> str:
    return 'Spetrum'

APP.run()
