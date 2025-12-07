from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class TuringMachine:
    def __init__(self, input_string):
        self.tape = list(input_string.lower()) + ["_"]
        self.head = 0
        self.state = "q0"
        self.vowel_count = 0

    def step(self):
        symbol = self.tape[self.head]

        if self.state == "q0":
            if symbol in "aiueo":
                self.vowel_count += 1
                self.head += 1
            elif symbol == "_":
                self.state = "qAccept"
            else:
                self.head += 1

        return self.state != "qAccept"

    def run(self):
        while self.step():
            pass
        return self.vowel_count


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hitung", methods=["POST"])
def hitung():
    data = request.json
    text = data.get("text", "")

    tm = TuringMachine(text)
    result = tm.run()

    return jsonify({
        "input": text,
        "vokal": result
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
