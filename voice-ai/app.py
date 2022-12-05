import os
import openai
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Use the CORS extension to enable CORS for the app
CORS(app)

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/answer/<question>')
def answer_question(question):
    response = openai.Completion.create(
        prompt=question,
        engine="text-davinci-003",  # use the "text-davinci-003" engine
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=1,
        max_tokens=150
    )

    # Check if the response has a valid answer
    if len(response['choices']) == 0 or 'text' not in response['choices'][0]:
        return "Sorry, I couldn't find an answer to your question."

    answer = response['choices'][0]['text']
    return answer.strip()

if __name__ == '__main__':
    app.run()
