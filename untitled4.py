# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:13:55 2021

@author: escc1122
"""

from flask import Flask
from flask import request
from flask import render_template
from pythainlp.tokenize import multi_cut

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    Text = request.args.get('Text')
    
    return c1(Text)+divider()+c2(Text)

@app.route('/test',methods=['GET'])
def test():
    return render_template("index.html")


def divider():
    return "<br>==========================================<br>"

def c1(Text):
    return Text.replace('\r\n', '<br>')


def c2(Text):
    colors = ["Black","Red"]
    r = ""
    text_array = Text.split('\r\n')
    for idx, v in enumerate(text_array):
        segmens = multi_cut.segment(v)
        k1 = ''
        k2 = ''
        for idx2, v2 in enumerate(segmens):
            k1 = k1 + v2 + "<br>"
            k2 = k2 + "<span style='color:"+colors[idx2%2]+";display: inline-block;'>" + v2 + "</span>"
        r = r + v + "<br>"     
        r = r + k2 + "<br>"
        r = r + k1 + "<br>"    
        r = r + divider()
        r = r + "<br><br>"

    
    return r




app.run(host="0.0.0.0",port=int("8085"))
