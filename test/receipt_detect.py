import os
import unittest
import detecttext

class Receipt(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.receipt_path = os.path.abspath('bin/receipt3.jpg')

    def isReceipt(self):
        detecttext.checkReceipt(self.receipt_path)