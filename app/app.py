from flask import Flask, jsonify
import os
import openai
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)