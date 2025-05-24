from flask import Flask, jsonify
from bot import pending_signals

app = Flask(__name__)

@app.route("/sinais")
def sinais():
    return jsonify(pending_signals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)