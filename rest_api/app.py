from flask import Flask, jsonify, request

from db import DataBase
from db.create_db import ComicRow

app = Flask(__name__)


@app.route("/api/create_new_table", methods=['POST'])
def create_table():
    api_details = request.get_json()
    name = api_details["name"]
    result = DataBase.create_new_comic(str(name), 1)
    return jsonify(result)


@app.route("/api/update_table", methods=['PUT'])
def update_table():
    api_details = request.get_json()
    name = api_details["table_name"]
    data_to_row = api_details["photo_url"]
    if data_to_row.split('.')[-1] not in ["jpg", "jpeg", "png"]:
        return jsonify("not image url")
    result = DataBase.write_data(name, ComicRow(data_to_row), mode=1)
    return jsonify(result)


@app.route("/api/delete_table", methods=['DELETE'])
def delete_table():
    api_details = request.get_json()
    table_name = api_details["table_name"]
    res = DataBase.delete_table(table_name, mode=1)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
