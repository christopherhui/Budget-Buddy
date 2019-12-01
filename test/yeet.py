import io
import os

receipt_path = os.path.abspath('../bin/receipt3.jpg')

# Loads the image into memory
with io.open(receipt_path, 'rb') as image_file:
    content = image_file.read()
print(content)