from flask import Flask


from flask_restful import Resource
from flask import jsonify
import sqlite3
from api import app
from helper_functions import find_name

class Receipt(Resource):
    def getTotal(self, receipt):
        """
        :param receipt: the receipt
        :return: total
        """
        
        return textDetection(receipt)