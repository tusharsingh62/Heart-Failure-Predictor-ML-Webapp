# Importing essential libraries
from flask import Flask, render_template, request
import jsonify
import pickle
import numpy as np


# Load the Random Forest CLassifier model
model_name = 'RF_model.pkl'
classifier = pickle.load(open(model_name, 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        creatinine_phosphokinase = int(request.form['creatinine_phosphokinase'])
        ejection_fraction = int(request.form['ejection_fraction'])
        platelet_cnt = float(request.form['platelet'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium  = int(request.form['serum_sodium'])
        times = int(request.form['time'])
        anaemia = request.form['anaemia']
        if anaemia == 'YES':
            anaemia = 1
        else:
            anaemia = 0
        diabetes = request.form['diabetes']
        if diabetes == 'YES':
            diabetes = 1
        else:
            diabetes = 0
        high_blood_pressure = request.form['high_blood_pressure']
        if high_blood_pressure == 'YES':
            high_blood_pressure = 1
        else:
            high_blood_pressure = 0
        sex = request.form['sex']
        if sex == 'MALE':
            sex = 1
        else:
            sex = 0
        smoking = request.form['smoking']
        if smoking == 'YES':
            smoking = 1
        else:
            smoking = 0
            
        predict = classifier.predict([np.array([age, anaemia,creatinine_phosphokinase, diabetes, ejection_fraction,high_blood_pressure,platelet_cnt, serum_creatinine, serum_sodium, sex, smoking, times])])
        return render_template('result.html',prediction=predict[0])
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
        
        
            
            
            
            
        
    
