from Items.Funciones import preprocessing_dataframe, feature_selection
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from pickle import load

def intro():
        st.image("https://esports.eldesmarque.com/wp-content/uploads/2019/09/LoL2.jpg", use_column_width = True)
        c1, c2 = st.columns(2)
        with c1:
            boton_1 = st.button("¿Qué es el LoL?", key = "LoL")
        
        if boton_1 == True:
            st.write("El LoL (League of Legends) es un videojuego competitivo por equipos. En este, el objetivo consiste en llegar los primeros a la base enemiga y destruir la estructura conocida como 'Nexo'. Quien primero lo haga, gana./nLa mecánica parece simple, pero implica mucho más. Hay dragones que otorgan ventajas a quienes los vencen; existen heraldos y barones que generan también efectos positivos de una u otra manera; existen objetos que otorgan diferentes estadísticas.../n¡El juego puede llegar a ser tan complicado que los jugadores han dividido la teoría de éste en lo que se conoce como 'macrogame' y 'microgame'!/nUna auténtica locura, pero en este proyecto nos proponemos a generar una predicción fiable de qué equipo ganará introduciendo unos datos clave.")
        
        with c2:
            boton_2 = st.button("Metodología aplicada", key = "Method")
        
        if boton_2 == True:
            st.write(f"La metodología empleada para alcanzar el objetivo propuesto ha consistido en estudiar minuciosamente los datos y la teoría subyacente al juego. Originalmente se contaba con un dataset con un total de 57 columnas. Es decir, 57 variables potenciales./nDebido a la inviabilidad de preguntar al usuario por 57 datos concretos, y sabiendo que no todos son igual de relevantes, estas variables se redujeron a 12 empleando las Feature Importances de un modelo de Machine Learning conocido como ExtraTrees, que empleaba, para este propósito, un total de 200 estimadores./nAl reducir a 12 las variables por orden de importancia, se decidió probar diferentes modelos de Machine Learning, encontrando que un modelo de Boosting (HistGradientBoosting) con parámetros estándar obtenía las siguientes métricas:")
            st.markdown("- Accuracy: 97%")
            st.markdown("- Jaccard Index: 93%")
            st.markdown("- Precisión: 97%")
            st.markdown("- Sensibilidad: 97%")
            st.markdown("- F1-Score: 97%")
            st.write("Además, presentaba la siguiente matriz de confusión:")
            st.image("Data/matriz_de_confusion.png")
            st.write(f"Finalmente, se ha comprobado que estos buenos resultados no han sido producto de un sobreentrenamiento, pues al realizar una validación cruzada, empleando K-Fold con 100 splits, hemos obtenido un resultado promedio de 97% de accuracy.")
            st.write(f"Todo esto nos dice que tenemos un modelo que es bastante exacto a la hora de predecir; que posee una gran capacidad de separar verdaderos de falsos positivos (precisión), además de verdaderos positivos de falsos negativos (sensibilidad) y que, en total, se equivoca un 3% de las veces. Su pérdida de logarítmica es de 0.06, lo que indica una elevada probabilidad de que sus predicciones se cumplan. Por ende, consideramos haber entrenado un modelo bastante fiable.")
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
        
    model = load(open("Data/Modelo_seleccionado.sav", "rb"))
    
    if submitted:
        variables = (t2_tower, t1_tower, inhibitor, t2_inhibitor, t1_inhibitor, tower, baron, t2_dragon, t1_dragon, t1_baron, t2_baron, dragon)
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
def conclusion():
    st.image("https://miro.medium.com/v2/resize:fit:679/1*H4cW-_RCyHpu5FNtVaAPoQ.gif")
    st.markdown("**¡Muy bien!**")
    st.write("Ahora que has llegado hasta aquí, conoces cómo se ha elaborado el proyecto, en qué consiste y qué uso puedes darle. Sin embargo, pasaremos a comentar algunas conclusiones que nos ha dado a entender el proyecto y que son bastante interesantes. Además, si te interesa contactarme te dejo mi perfil de LinkedIn ;)")
    c1, c2 = st.columns(2)
    with c1:
        boton_1 = st.button("Conclusiones", key = "Conclusion_page")
    with c2:
        boton_2 = st.button("Sobre mí", key = "about_me")
    if boton_1 == True:
        st.write("Elaborando este modelo, se ha encontrado que las variables más relevantes para predecir la victoria de un equipo son tan universales como:")
        st.markdown("- Torres eliminadas")
        st.markdown("- Inhibidores eliminados")
        st.markdown("- Barones ejecutados")
        st.markdown("- Dragones ejecutados")
        st.write("Ante esto, encontramos que existe un enorme peso por parte de las variables grupales (objetivos realizados) por encima de las individuales (asesinatos, asistencias, oro obtenido...), de modo que esto nos indica que es mucho más decisivo saber gestionar el llamado 'macro-game' antes que el 'micro-game' y que, por tanto, los jugadores brillan más siendo jugadores de equipo, cooperativos y centrados en ayudar a lograr objetivos que aquellos que son individualmente buenos, pero no contribuyen a su equipo de la misma manera.")
        st.write("Ganar una ventaja competitiva, por ende, se vuelve más importante que jugar individualmente bien las mecánicas de algún campeón en concreto.")
        st.write("Además, esto nos induce a concluir que, si bien, el modelo debe ser actualizado constantemente según se obtienen nuevos datos de partidas, éste puede servir de forma universal a las diferentes temporadas o, 'seasons' del juego.")
    if boton_2 == True:
        st.write("¡Hola! Si te preguntas quién soy, brevemente te diré que soy un científico de datos y economista (graduado y colegiado, sí), pero ante todo un friki de los datos. No tengo problemas en admitirlo. ¡Amo el mundo analítico! Tanto que pienso en él a diario, busco siempre aprender algo nuevo y pienso en cómo enfocar diferentes problemas, desde cotidianos a no cotidianos, usando este tipo de enfoque (sí, no era una exageración lo de que soy un friki de los datos jaja)")
        st.write("Si tienes alguna duda, quieres que charlemos o, incluso, eres algún profesional y consideras que puedo cubrir alguna vacante en tu compañía y aportaros valor, ¡no dudes en contactarme!")
        st.image("https://1000marcas.net/wp-content/uploads/2020/01/Logo-Linkedin.png")
        url = "Ya sabes... [¡Click aquí!](www.linkedin.com/in/adrián-chávez)"
        st.write(url, unsafe_allow_html = True)

def main():
    st.set_page_config(page_title="Predicción de equipo ganador", page_icon="🏆")
    st.title("¿Quién va a ganar esta partida?")
    st.header("¡Hola!")
    st.write("Para seleccionar una página, usa el desplegable a tu izquierda. Si no lo ves, recuerda que solo tienes que hacer click en la palomita de la esquina superior izquierda para poder ver dicho desplegable.")
    st.write("Cuentas con una introducción para saber de qué va este juego si aún no lo conoces y/o para conocer la metodología que se ha empleado en este proyecto y conocer de su fiabilidad.")
    st.write("También cuentas con la página del proyecto, obviamente; y con una página de conclusiones por si quieres contactar conmigo o conocer algún datillo extra interesante de este proyecto ;)")
    
    selected_page = st.sidebar.selectbox("Selecciona una página", ["Introducción", "Proyecto", "Conclusiones"])
    
    if selected_page == "Introducción":
        intro()
    elif selected_page == "Proyecto":
        project()
    elif selected_page == "Conclusiones":
        conclusion()

if __name__ == "__main__":
    main()