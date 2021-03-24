# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:17:59 2021

@author: Anagha
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__)
model = pickle.load(open(r'C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Random_Forest.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features=[float(x) for x in request.form.values()]
    final_features=[np.array(features)]
    pre=model.predict(final_features)
    
    output = round(pre[0], 2)
    if(output >=2.5):

        return render_template('index.html', prediction_text='Air Quality Index is $ {} and air have bad  quality'.format(output))
    else:
         return render_template('index.html', prediction_text='Air Quality Index is $ {} and air have good quality'.format(output))


if __name__ == "__main__":
    app.run(debug=True)