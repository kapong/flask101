from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload'

@app.route('/size', methods=['POST']) 
def checkimage():
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
    
    w, h = img.size
    
    return jsonify({
        "size": {
            "w": w,
            "h": h,
        }
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
