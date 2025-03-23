from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.o6_model_prediction import model_prediction


app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index_homepage():
    return render_template('index.html')


@app.route('/Train',methods = ['GET'])
def train_model():
    # os.system("python main.py")
    return"prediction successful"

@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        try :
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
                    total_sulfur_dioxide,density,pH,sulphates,alcohol]
            
            data = np.array(data).reshape(1,11)

            obj = model_prediction()
            prediction1 = obj.predict(data)

            return render_template('result.html',prediction = str(prediction1))
        except Exception as e :
            return "something is wrong"
        
    else :
        return render_template('index.html')
    



if __name__ == '__main__':
    app.run(debug=True)