from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = load_model("output/cifar10_cnn_hypertuned_model.h5")

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# CIFAR-10 sınıf etiketleri
labels = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
          'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

def prepare_image(image_path):
    img = Image.open(image_path).resize((32, 32))
    img = img_to_array(img)
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_path = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            img = prepare_image(image_path)
            preds = model.predict(img)
            predicted_class = labels[np.argmax(preds)]
            prediction = f"Prediction: {predicted_class}"

    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
