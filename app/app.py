from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import os
import openai
import json
import time

app = Flask(__name__)

# Make sure .env has valid key for JWT_SECRET_KEY
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Make .env has valid key for OPENAI_API_KEY 
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Give auth'd users a token
@app.route('/login', methods=['POST'])
def token():
    # Get user and pass from request
    username = request.json.get('username')
    password = request.json.get('password')

    # 'test' for demonstration purposes
    if username != 'test' or password != 'test':
        return {'message': 'Invalid credentials'}, 401

    # Create and return token to user
    access_token = create_access_token(identity=username)
    return {'access_token': access_token}, 200

# Serve request only if a valid token is included
@app.route('/', methods=['POST'])
@jwt_required()
def chat():
    # Time the reqest
    start_time = time.time()

    # Pass user input to Chat GPT-3    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request.json["input_text"]},
        ],
        temperature=0,
    )

    # Return the response
    response = response["choices"][0]["message"]["content"]
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)