from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/comics', methods=['GET'])
def hello_world():  # put application's code here
    comics = [
        {"id": 1, "url": "https://5"},
        {"id": 2, "url": "https://q"},
    ]
    return jsonify({"comics": comics})


if __name__ == '__main__':
    app.run(debug=True)
