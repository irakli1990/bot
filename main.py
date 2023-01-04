# This is a sample Python script.
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import jsonify, Flask, request

app = Flask('Chat boot')

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")


@app.post("/ask")
def get_answer():
    question = request.get_json()['question']
    answer = {"message": str(chatbot.get_response(question))}
    return jsonify(answer)


@app.get("/version")
def get_version():
    version = {"version": '1.0.0'}
    return jsonify(version)

@app.route("/")
def index():
    version = {"version": '1.0.0'}
    return jsonify(version)


if __name__ == '__main__':
    app.run(debug=True)
