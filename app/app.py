from flask import Flask, request
import os
import openai
import json
import time

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def chat():
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request.json["input_text"]},
        ],
        temperature=0,
    )
    end_time = time.time()
    duration = end_time - start_time
    duration = round(duration, 2)
    response = "\n" +response["choices"][0]["message"]["content"] + "\n" + "Load:" + str(duration) + "sec" + "\n" + "\n"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)