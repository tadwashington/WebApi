from flask import Flask, request, render_template, redirect, url_for, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
import platform

app = Flask(__name__)
# 文字化けを防止
app.config['JSON_AS_ASCII'] = False;


@app.route("/api_get/<key>", methods=["GET"])
def api_get(key):
    data = {key: []}
    r = {"error_code": "0001"}
    data[key].append(r)
    r = {"error_message": "パラメータが正しくありません。"}
    data[key].append(r)
    return jsonify(data)


if __name__ == "__main__":
    print("おpythonの御バージョンは= " + platform.python_version() + "でんガス。\r\n")
    # app.run()
    app.run(debug=False, host='localhost', port=29294)
