########################################################################################################################################
# SCRIPT NAME:             FlaskApi.py                                                                                                 #
# AUTHOR NAME:             NAMAN SINGHAI                                                                                               #
# FUNCTIONALITY:           FLASK API                                                                                                   #
# DEVELOPMENT ENVIRONMENT: C:\Python\Python39\PythonDev\Scripts\activate                                                               #
########################################################################################################################################


# import pandas as pd
from flask import Flask, request
# from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "THIS IS A FLASK API"
    }
