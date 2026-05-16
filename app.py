from flask import Flask, render_template, request, redirect
import os

from hashing import hash_id
from encrypt import encrypt_image
from decrypt import decrypt_image
from database import insert_data, get_data, get_all_data

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    records = get_all_data()
    return render_template("index.html", records=records)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    patient_id = request.form["patient_id"]

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    patient_hash = hash_id(patient_id)

    encrypted_data, key = encrypt_image(filepath)

    insert_data(patient_hash, encrypted_data, key)

    return redirect("/")


@app.route("/view/<int:id>")
def view(id):
    result = get_data(id)

    if result is None:
        return "❌ No data found"

    data, key = result

    output_path = os.path.join("static", "uploads", "decrypted.jpg")

    decrypt_image(data, key, output_path)

    return render_template("view.html", image="uploads/decrypted.jpg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)