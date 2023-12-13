import os

import tensorflow as tf
from tensorflow import keras
import numpy as np

from flask import Flask, jsonify, request

model = keras.models.load_model("model_1.h5")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict_new_data():
    if request.method == "POST":
        try:
            data = request.get_json()

            AR16 = data.get('AR16')
            KR03 = data.get('KR03')
            KR11 = data.get('KR11')
            KR13 = data.get('KR13')
            KR20 = data.get('KR20')
            KR24 = data.get('KR24')
            KR26 = data.get('KR26')
            KRK06 = data.get('KRK06')
            KRK08 = data.get('KRK08')
            KRK09 = data.get('KRK09')
            KRK10 = data.get('KRK10')

            input_data = [AR16, KR03, KR11, KR13, KR20, KR24, KR26, KRK06, KRK08, KRK09, KRK10]

            input_array = np.array(input_data).reshape(1, -1)
            predictions = model.predict(input_array)
            threshold = 0.5
            binary_predictions = (predictions >= threshold).astype(int)
            result = int(binary_predictions.flatten()[0])

            response = {"result": result}
            return jsonify(response)

        except Exception as e:
            return jsonify({"error": str(e)})
    
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
