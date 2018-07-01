from flask import Flask, render_template, jsonify
from random import randint
from flask_cors import CORS

app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
