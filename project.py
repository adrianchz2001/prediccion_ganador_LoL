import pickle
import streamlit as st
import numpy as np
import pandas as pd
import sklearn

def project():
    with st.form("Introduce los datos:"):
        st.write("*Recuerda comprobar si has aparecido en el lado del equipo azul o del equipo rojo*")
        
        tower = st.selectbox("¿Quién ha destruido la primera torre?", options = ["Azul", "Rojo", "Nadie"])
        
        if tower == "Azul":
            tower = 1
            
        elif tower == "Rojo":
            tower = 2
            
        else:
            tower = 0
            
        t2_tower = st.number_input("¿Cuántas torres ha destruido el equipo rojo?", min_value = 0, max_value = 11)
        t1_tower = st.number_input("¿Cuántas torres ha destruido el equipo azul?", min_value = 0, max_value = 11)
        
        inhibitor = st.selectbox("¿Quién ha destruido el primer inhibidor?", options = ["Azul", "Rojo", "Nadie"])
        
        if inhibitor == "Azul":
            inhibitor = 1
            
        elif inhibitor == "Rojo":
            inhibitor = 2
            
        else:
            inhibitor = 0
            
        t2_inhibitor = st.number_input("¿Cuántos inhibidores ha destruido el equipo rojo?", min_value = 0, max_value = 3)
        t1_inhibitor = st.number_input("¿Cuántos inhibidores ha destruido el equipo azul?", min_value = 0, max_value = 3)
        
        baron = st.selectbox("¿Quién ha matado primero al baron?", options = ["Azul", "Rojo", "Nadie"])
        
        if baron == "Azul":
            baron = 1
        elif baron == "Rojo":
            baron = 2
        else:
            baron = 0
            
        dragon = st.selectbox("¿Quién ha matado al primer dragon?", options = ["Azul", "Rojo", "Nadie"])
        
        if dragon == "Azul":
            dragon = 1
        elif dragon == "Rojo":
            dragon = 2
        else:
            dragon = 0
            
        t1_baron = st.number_input("¿Cuántos barones ha matado el equipo azul?", min_value = 0, max_value = 2)
        t2_baron = st.number_input("¿Cuántos barones ha matado el equipo rojo?", min_value = 0, max_value = 2)
        
        t1_dragon = st.number_input("¿Cuántos dragones ha matado el equipo azul?", min_value = 0, max_value = 6)
        t2_dragon = st.number_input("¿Cuántos dragones ha matado el equipo rojo?", min_value = 0, max_value = 6)
        
        submitted = st.form_submit_button("Ejecutar")
    
    if submitted:
        variables = (t2_tower, t1_tower, inhibitor, t2_inhibitor, t1_inhibitor, tower, baron, t2_dragon, t1_dragon, t1_baron, t2_baron)
        variables = np.array(variables).reshape(1, -1)
        yhat = model.predict(variables)[0]
        if yhat == 1:
            st.write("El modelo predice que ganará el equipo azul")
            st.markdown(f"Probabilidad: **{round(model.predict_proba(variables)[0][0]*100, 2)}%**")
            estilo_fondo = "background-color: blue;"
            st.markdown(f'<style>{estilo_fondo}</style>', unsafe_allow_html=True)
            
        if yhat == 2:
            st.write("El modelo predice que ganará el equipo rojo")
            st.markdown(f"Probabilidad: **{round(model.predict_proba(variables)[0][1]*100, 2)}%**")
            estilo_fondo = "background-color: red;"
            st.markdown(f'<style>{estilo_fondo}</style>', unsafe_allow_html=True)