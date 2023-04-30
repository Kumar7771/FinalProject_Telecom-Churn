from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


app = Flask(__name__)
model = pickle.load(open('churnmodel.pkl', 'rb'))



@app.route("/")
def hello():
    return render_template('index.html')
# @app.route('/',methods=['GET'])
# def Home():
#     return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    internetservice_No=0
    contract_Two_year=0
    paymentmethod_Electronic_check=0
    paymentmethod_Mailed_check=0
    if request.method == 'POST':

        seniorcitizen = int(request.form['seniorcitizen'])
        tenure = int(request.form['tenure'])
        monthlycharges = float(request.form['monthlycharges'])
        gender_Male =request.form['gender_Male']
        if(gender_Male =='Male'):

            gender_Male=1
        else:
            gender_Male=0

        partner_Yes =request.form['partner_Yes']
        if(partner_Yes =='Yes'):
        
            partner_Yes=1
        else:
            partner_Yes=0

        phoneservice_Yes =request.form['phoneservice_Yes']
        if(phoneservice_Yes =='Yes'):
        
            phoneservice_Yes=1
        else:
            phoneservice_Yes=0	
        

        internetservice_Fiber_optic=request.form['internetservice_Fiber_optic']
        if(internetservice_Fiber_optic=='Fiber_optic'):
        
            internetservice_Fiber_optic=1
            internetservice_No=0
        elif(internetservice_Fiber_optic=='No'):
            internetservice_Fiber_optic=0
            internetservice_No=1
        else:
            internetservice_Fiber_optic=0
            internetservice_No=0

        contract_One_year=request.form['contract_One_year']
        if(contract_One_year=='One_year'):
            
            contract_One_year=1
            contract_Two_year=0
        elif(contract_One_year=='Two_year'):
            contract_One_year=0
            contract_Two_year=1
        else:
            contract_One_year=0
            contract_Two_year=0

        paperlessbilling_Yes =request.form['paperlessbilling_Yes']
        if(paperlessbilling_Yes =='Yes'):
            paperlessbilling_Yes=1
        else:
            paperlessbilling_Yes=0

        paymentmethod_Credit_card_automatic=request.form['paymentmethod_Credit_card_automatic']
        if(paymentmethod_Credit_card_automatic=='Credit_card_automatic'):
            paymentmethod_Credit_card_automatic=1
            paymentmethod_Electronic_check=0
            paymentmethod_Mailed_check=0
        elif(paymentmethod_Credit_card_automatic=='Electronic_check'):
            paymentmethod_Credit_card_automatic=0
            paymentmethod_Electronic_check=1
            paymentmethod_Mailed_check=0
        elif(paymentmethod_Credit_card_automatic=='Mailed_check'):
            paymentmethod_Credit_card_automatic=0
            paymentmethod_Electronic_check=0
            paymentmethod_Mailed_check=1
        else:
            paymentmethod_Credit_card_automatic=0
            paymentmethod_Electronic_check=0
            paymentmethod_Mailed_check=0


        prediction = model.predict([[seniorcitizen, tenure, monthlycharges,gender_Male,partner_Yes,phoneservice_Yes,internetservice_Fiber_optic,internetservice_No,contract_One_year,contract_Two_year,paperlessbilling_Yes,paymentmethod_Credit_card_automatic,paymentmethod_Electronic_check,paymentmethod_Mailed_check]])
        output = prediction[0]
        return render_template('index.html', prediction_text = f" Person will be churned or not? : {output}")

    else:
        return render_template('index.html')

        



if __name__ == "__main__":
        app.run()

    
