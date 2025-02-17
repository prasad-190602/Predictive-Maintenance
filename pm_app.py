# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:39:46 2025

@author: karan
"""

import pickle
import streamlit as st

st.title('Predictive Maintenance')

load = open('pm_final_model9.pkl','rb')
model = pickle.load(load)

def predict(Type, Air_Temperature, Process_Temperature, Rotational_Speed, Torque, Tool_Wear, TWF, HDF, PWF, OSF, RNF):
    prediction = model.predict([[Type, Air_Temperature, Process_Temperature, Rotational_Speed, Torque, Tool_Wear, TWF, HDF, PWF, OSF, RNF]])
    return prediction

def main():
    st.markdown("Will we need to do maintenance? Let's find out!")
    
    # Single-row selection for Type
    Type = st.selectbox('Type', ("L", "M", "H"))
    
    # Two-column layout for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        Air_Temperature = st.number_input('Air Temperature (K)', help='Enter Air Temperature in K')
        Process_Temperature = st.number_input('Process Temperature (K)', help='Enter Process Temperature in K')
        Rotational_Speed = st.number_input('Rotational Speed (rpm)', format="%.0f", help='Enter Rotational Speed in rpm')
        Torque = st.number_input('Torque (Nm)', help='Enter Torque in Nm')
        Tool_Wear = st.number_input('Tool Wear (min)', format="%.0f", help='Enter Tool Wear in min')
    
    with col2:
        TWF = st.selectbox('Tool Wear Failure', (0, 1), help='Tool Wear Failure')
        HDF = st.selectbox('Heat Dissipation Failure', (0, 1), help='Heat Dissipation Failure')
        PWF = st.selectbox('Power Failure', (0, 1), help='Power Failure')
        OSF = st.selectbox('Overstrain Failure', (0, 1), help='Overstrain Failure')
        RNF = st.selectbox('Random Failure', (0, 1), help='Random Failure')
    
    if st.button('Predict'):
        result = predict(Type, Air_Temperature, Process_Temperature, Rotational_Speed, Torque, Tool_Wear, TWF, HDF, PWF, OSF, RNF)
        if result == 0:
            st.success("✅ Maintenance NOT Required for Machine")
        else:
            st.error("⚠️ Maintenance REQUIRED for Machine ")

if __name__ == '__main__':
    main()
