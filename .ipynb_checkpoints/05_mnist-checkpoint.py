from PIL import Image
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

from mymnist import recognize_mnist

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload'

@app.route('/mnist', methods=['POST']) 
def mnist():
    try:
        imgfile = request.files['image']
        filename = secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except:
        return jsonify({
            "error": "File Error!",
        }), 400
    
    try:
        img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({
            "error": "Not an image!",
        }), 400
    
    res_class, res_prob = recognize_mnist(img)
    
    return jsonify({
        "class": res_class,
        "probs": res_prob,
    })

def fibo(num):
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

if __name__ == '__main__':
    app.run()
