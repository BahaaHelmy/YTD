# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytube
# ------------------------(import libraries)------------
import numpy as np
from flask import Flask, request, render_template

# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def Home():
    return render_template("Prediction.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    strr = [x for x in request.form.values()]
    print(strr)
    link = pytube.YouTube(strr[0])
    status=link.streams.filter(file_extension='mp4', res="360p").first().download()
    print(status)
    return render_template("Prediction.html", prediction_text=status)


if __name__ == "__main__":
    flask_app.run(debug=True)
