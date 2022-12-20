from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import os
import sys
import glob
import re
import numpy as np
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.utils.image_utils import load_img, img_to_array


app = Flask(__name__)
model_path = "resnet.h5"
model = load_model(model_path)


def model_predict(img_path, model):
    img = load_img(img_path, target_size=(224, 224))

    x = img_to_array(img)

    x = x / 255
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)
    pred = np.argmax(pred, axis=1)
    if pred == 0:
        pred = "The Car iS Audi"
    elif pred == 1:
        pred = "The Car is Lamborghini"
    else:
        pred = "The Car Is Mercedes"

    return pred


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        # return result
        return render_template("index.html", prediction_text= str(result))
    return None


if __name__ == '__main__':
    app.run(debug=True)