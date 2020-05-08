from PIL import Image
import tensorflow as tf
# Helper libraries
import numpy as np

model = tf.keras.models.load_model('model/mnist_model')
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def recognize_mnist(img):
    img = img.resize((28,28))
    img = np.array(img)
    img = img[:,:,0]
    xmax = np.max(img)
    xmin = np.min(img)
    img = (xmax - img)/(xmax - xmin)
    predictions = probability_model.predict([[img]])
    return class_names[np.argmax(predictions)], dict(zip(class_names, [float(p*100) for p in predictions[0]]))