from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return jsonify({"message": "It Works"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)