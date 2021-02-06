########################################################################################################################################
# SCRIPT NAME:             FlaskApi.py                                                                                                 #
# AUTHOR NAME:             NAMAN SINGHAI                                                                                               #
# FUNCTIONALITY:           FLASK API                                                                                                   #
# DEVELOPMENT ENVIRONMENT: C:\Python\Python39\PythonDev\Scripts\activate                                                               #
########################################################################################################################################


import pandas as pd
from datetime import datetime as dt
from flask import Flask, request


data = pd.read_csv("E:\Downloads\FlaskAPI\Monarchs-of-England.csv", names=["s", "e", "m"]).set_index("m")

series = pd.Series(index=range(data.s.min(), dt.now().year))

for m in data.index:
    series.loc[data.loc[m].s:data.loc[m].e] = m

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    year = int(request.args["year"])
    try:
        return "THIS IS MY HOME PAGE"
    except Exception as e:
        print(f"EXCEPTION RAISED: {e}")


