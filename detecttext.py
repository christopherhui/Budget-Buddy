import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Import the base64 encoding library.
import base64

# Pass the image data to an encoding function.
def encode_image(image):
  image_content = image.read()
  return base64.b64encode(image_content)

def checkReceipt(path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    print(response)
    labels = response.label_annotations

    # Check if there is a receipt
    found = False
    for label in labels:
        if label.description == 'Receipt':
            found = True

    if not found:
        raise Exception('Image does not contain a receipt')

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    # print(texts)

    # for text in texts:
        # print('\n"{}"'.format(text.description))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        #
        # print('bounds: {}'.format(','.join(vertices)))

    print(get_total(texts[0].description.split()))

def get_total(textArr):
    maxFloat = 0.0
    for text in textArr:
        # Check that it can be parsed to float
        try:
            tF = float(text)
            if isItMoney(text):
                maxFloat = max(maxFloat, tF)
        except:
            pass
    return maxFloat

def isItMoney(text):
    # Check if it is a float with two decimal places, to see if it is a price
    isItMoney = text.split(".")
    return len(isItMoney) == 2 and isItMoney[1].isdigit()

path = os.path.abspath('bin/receipt1.jpg')
checkReceipt(path)
detect_text(path)