from crypt import methods
from turtle import update
from flask import Flask, request
import numpy as np 
import pickle 
from flasgger import Swagger
import pandas as pd
app = Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
        
    """
    # df_test = pd.read_csv(request.files.get("file")) 
    # Inside your route function
    file = request.files.get("file")
    if not file:
        return "No file found", 400

    try:
        df_test = pd.read_csv(file)
    except Exception as e:
        return str(e), 400
    
    prediction = classifier.predict(df_test)
    return "The predicted value for the csv is " + str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
