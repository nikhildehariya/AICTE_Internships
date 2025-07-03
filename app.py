# Import all libraries 

import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st
# Load the model and structure
model = joblib.load("water_quality_model.pkl")
model_cols = joblib.load("feature_columns.pkl")


# Let's Create User Interface of App

st.title("Water Quality Predictor")
st.write("This app predicts the quality of water based on Year and Station ID.")

# user inputs
year = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID", value = '1')

# to encode and then predict


if st.button("Predict"):
   if not station_id:
       st.warning("Please Enter a Station ID")
   else:
       # Prepare the Input 
       input_df = pd.DataFrame({"Year": [year],"Station ID": [station_id]})
       input_encoded = pd.get_dummies(input_df, columns=["Station ID"])
       
       # Align with model cols
       for col in model_cols:
           if col not in  input_encoded.columns:
               input_encoded[col] = 0
       input_encoded = input_encoded[model_cols]      
        
       # Predict
       predicted_pollutants = model.predict(input_encoded)[0]
       pollutants = ['O2','NO3','NO2','SO4','PO4','CL','NH3']
        
       st.subheader(f"Predicted Pollutant Level For Station'{station_id}' in {year}:")
       predicted_values = {}
       for p, val in zip(pollutants, predicted_pollutants):
           st.write(f'{p}: {val:.2f}')
        
       chart_df = pd.DataFrame(predicted_pollutants, index=pollutants, columns=["Level"])
       st.line_chart(chart_df)
        
    
                    
