from PIL import Image
# Helper libraries
import numpy as np

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def recognize_mnist(img):
    predictions = np.random.random((1,10))
    return class_names[np.argmax(predictions)], dict(zip(class_names, [float(p*100) for p in predictions[0]]))