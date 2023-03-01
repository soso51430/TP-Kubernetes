from flask import Flask

import random

app = Flask(__name__)

messages = [
    "Bonjour !",
    "Bonne journée !",
    "Hello World !",
]

@app.route('/')
def get_message():
    message = "Voici le message du jour : " + random.choice(messages)
    return message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
