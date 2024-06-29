# -*- coding: utf-8 -*-

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
loaded_model = pickle.load(open('trained_model_All.sav', 'rb'))
loaded_model_1 = pickle.load(open('trained_model_Amikacin.sav', 'rb'))
loaded_model_2 = pickle.load(open('trained_model_Aztreonam.sav', 'rb'))
loaded_model_3 = pickle.load(open('trained_model_Levofloxacin.sav', 'rb'))
loaded_model_4 = pickle.load(open('trained_model_Tigecycline.sav', 'rb'))
loaded_model_5 = pickle.load(open('trained_model_Colistin.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Select Antibiotic',

                          [                'Amikacin',
                           'Aztreonam','Levofloxacin','Tigecycline','Colistin','All Antibiotics'],
                          icons=['people','capsule','capsule','capsule','capsule','prescription2'],
                          default_index=0)
    
 

if(selected =='Amikacin'):
    #Page title
    st.title('Prediction for Amikacin')
    
    st.write('Please Enter the information about the patient:')
    # Getting the input data from user.

    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
    
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)
        
    

    # Code for prediction
    diagnosis_Amikacin = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        prediction_Amikacin = loaded_model_1.predict([[Age, Gender, Infection_Source, Condition, Infection_type]])
        if(prediction_Amikacin[0] == '0'):
            diagnosis_Amikacin = 'The person is Resistance to the Antibiotic'
        elif(prediction_Amikacin[0] == '1'):
            diagnosis_Amikacin ='The person is sensitive to the Antibiotic'
        elif(prediction_Amikacin[0] == '2'):
            diagnosis_Amikacin ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_Amikacin ='The person is Unknown to the Antibiotic'

    st.success(diagnosis_Amikacin)
    
if(selected =='Aztreonam'):
    #Page title
    st.title('Prediction for Aztreonam')
    
    st.write('Please Enter the information about the patient:')
    # Getting the input data from user.

    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
    
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)

    # Code for prediction
    diagnosis_Aztreonam = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        prediction_Aztreonam = loaded_model_2.predict([[Age, Gender, Infection_Source, Condition, Infection_type]])
        if(prediction_Aztreonam[0] == 0):
            diagnosis_Aztreonam='The person is Resistance to the Antibiotic'
        elif(prediction_Aztreonam[0] == 1):
            diagnosis_Aztreonam ='The person is sensitive to the Antibiotic'
        elif(prediction_Aztreonam[0] == 2):
            diagnosis_Aztreonamn ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_Aztreonam ='The person is Unknown to the Antibiotic'

    st.success(diagnosis_Aztreonam)
    
    
    
if(selected =='Levofloxacin'):
    #Page title
    st.title('Prediction for Levofloxacin')
    
    st.write('Please Enter the information about the patient:')
    # Getting the input data from user.

    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
        
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)

    # Code for prediction
    diagnosis_Levofloxacin = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        prediction_Levofloxacin = loaded_model_3.predict([[Age, Gender, Infection_Source, Condition, Infection_type]])
        if(prediction_Levofloxacin[0] == 0):
            diagnosis_Levofloxacin='The person is Resistance to the Antibiotic.'
        elif(prediction_Levofloxacin[0] == 1):
            diagnosis_Levofloxacin ='The person is sensitive to the Antibiotic.'
        elif(prediction_Levofloxacin[0] == 2):
            diagnosis_Levofloxacin ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_Levofloxacin ='The person is unknown to the Antibiotic.'

    st.success(diagnosis_Levofloxacin)
    
if(selected =='Tigecycline'):
    #Page title
    st.title('Prediction for Tigecycline')
    
    st.write('Please Enter the information about the patient:')
    # Getting the input data from user.

    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
    
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)

    # Code for prediction
    diagnosis_Tigecycline = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        prediction_Tigecycline = loaded_model_4.predict([[Age, Gender, Infection_Source, Condition, Infection_type]])
        if(prediction_Tigecycline[0] == 0):
            diagnosis_Tigecycline='The person is Resistance to the Antibiotic.'
        elif(prediction_Tigecycline[0] == 1):
            diagnosis_Tigecycline ='The person is sensitive to the Antibiotic.'
        elif(prediction_Tigecycline[0] == 2):
            diagnosis_Tigecycline ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_Tigecycline ='The person Unknown to the Antibiotic.'

    st.success(diagnosis_Tigecycline)
    
if(selected =='Colistin'):
    #Page title
    st.title('Prediction for Colistin')
    
    st.write('Please Enter the information abouto the patient:')
    # Getting the input data from user.

    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
    
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)

    # Code for prediction
    diagnosis_Colistin = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        prediction_Colistin = loaded_model_5.predict([[Age, Gender, Infection_Source, Condition, Infection_type]])
        if(prediction_Colistin[0] == 0):
            diagnosis_Colistin='The person is Resistance to the Antibiotic.'
        elif(prediction_Colistin[0] == 1):
            diagnosis_Colistin ='The person is sensitive to the Antibiotic.'
        elif(prediction_Colistin[0] == 2):
            diagnosis_Colistin ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_Colistin ='The person Unknown to the Antibiotic'

    st.success(diagnosis_Colistin)

#For all Antibiotics   
if(selected =='All Antibiotics'):
    #Page title
    st.title('Prediction for all Antibiotics')
    
    st.write('Please Enter the information about the patient:')
    # Getting the input data from user.
    col1, col2 = st.columns(2)
    
    with col1:
        Name = st.text_input('Name',max_chars=25)
        
    with col2:
        Patient_ID = st.number_input('Patient ID',value=0)
    
    with col1:
        Age = st.number_input('Age',4,110)
        
    with col2:
        Gender = st.number_input('Gender (Male=0 Female=1)',min_value=0, max_value=1,value=0)
    
    
    with col1:
        Infection_Source = st.number_input('Infection Source (ET ASPIRATE=0, PUS=1,BLOOD=2, TISSUE=3, WOUND SWAB=4, SPUTUM=5, URINE=6, TRACHEAL ASPIRATE=7)',min_value=0, max_value=7,value=0)
        
    with col2:
        Condition = st.number_input('Condition (Critical=0, Stable=1)',min_value=0, max_value=1,value=0)
    
    with col1:
        Infection_type = st.number_input('Infection_type (Hospital acquired=0,Community acquired=1)',min_value=0, max_value=1,value=0)
    
    with col2:
        Amikacin = st.number_input('Amikacin (Resistance=0, Sensitive=1, Intermediate=2, Unknown=3)',min_value=0, max_value=3,value=0)
    
    with col1:
        Aztreonam = st.number_input('Aztreonam (Resistance=0, Sensitive=1, Intermediate=2, Unknown=3)',min_value=0, max_value=3,value=0)
    
    with col2:
        Levofloxacin = st.number_input('Levofloxacin (Resistance=0, Sensitive=1, Intermediate=2, Unknown=3)',min_value=0, max_value=3,value=0)
    
    with col1:
        Tigecycline = st.number_input('Tigecycline (Resistance=0, Sensitive=1, Intermediate=2, Unknown=3)',min_value=0, max_value=3,value=0)
    
    with col2:
        Colistin = st.number_input('Colistin (Resistance=0, Sensitive=1, Intermediate=2, Unknown=3)',min_value=0, max_value=3,value=0)
    

    # Code for prediction
    diagnosis_all = ''

    # Creating a button for prediction

    if st.button('Antibiotic resistance result'):
        input_data =([Age, Gender, Infection_Source, Condition, Infection_type, Amikacin, Aztreonam, Levofloxacin, Tigecycline,
             Colistin])
        
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)
        
        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)
        
        if(prediction[0] == '0'):
            diagnosis_all='The person is Resistance to the Antibiotic.'
        elif(prediction[0] == '1'):
            diagnosis_all ='The person is sensitive to the Antibiotic.'
        elif(prediction[0] == '2'):
            diagnosis_all ='The person is intermediate to the Antibiotic.'
        else:
            diagnosis_all ='The person is Unknown to the Antibiotic'

    st.success(diagnosis_all)

    
