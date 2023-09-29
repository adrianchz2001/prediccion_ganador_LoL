import pandas as pd
import streamlit as st
import numpy as np

def conclusion():
    st.image("https://miro.medium.com/v2/resize:fit:679/1*H4cW-_RCyHpu5FNtVaAPoQ.gif")
    st.markdown("**¡Muy bien!**")
    st.write("Ahora que has llegado hasta aquí, conoces cómo se ha elaborado el proyecto, en qué consiste y qué uso puedes darle. Sin embargo, pasaremos a comentar algunas conclusiones que nos ha dado a entender el proyecto y que son bastante interesantes. Además, si te interesa contactarme te dejo mi perfil de LinkedIn ;)")
    c1, c2 = st.columns(2)
    with c1:
        boton_1 = st.button("Conclusiones", key = "Conclusion_page")
    with c2:
        boton_2 = st.button("Sobre mí", key = "about_me")
    if c1 == True:
        st.write("Elaborando este modelo, se ha encontrado que las variables más relevantes para predecir la victoria de un equipo son tan universales como:")
        st.markdown("- Torres eliminadas/n- Inhibidores eliminados/n- Dragones ejecutados/n- Barones ejecutados")
        st.write("Ante esto, encontramos que existe un enorme peso por parte de las variables grupales (objetivos realizados) por encima de las individuales (asesinatos, asistencias, oro obtenido...), de modo que esto nos indica que es mucho más decisivo saber gestionar el llamado 'macro-game' antes que el 'micro-game' y que, por tanto, los jugadores brillan más siendo jugadores de equipo, cooperativos y centrados en ayudar a lograr objetivos que aquellos que son individualmente buenos, pero no contribuyen a su equipo de la misma manera.")
        st.write("Ganar una ventaja competitiva, por ende, se vuelve más importante que jugar individualmente bien las mecánicas de algún campeón en concreto.")
        st.write("Además, esto nos induce a concluir que, si bien, el modelo debe ser actualizado constantemente según se obtienen nuevos datos de partidas, éste puede servir de forma universal a las diferentes temporadas o, 'seasons' del juego.")
    if c2 == True:
        st.write("¡Hola! Si te preguntas quién soy, brevemente te diré que soy un científico de datos y economista (graduado y colegiado, sí), pero ante todo un friki de los datos. No tengo problemas en admitirlo. ¡Amo el mundo analítico! Tanto que pienso en él a diario, busco siempre aprender algo nuevo y pienso en cómo enfocar diferentes problemas, desde cotidianos a no cotidianos, usando este tipo de enfoque (sí, no era una exageración lo de que soy un friki de los datos jaja)")
        st.write("Si tienes alguna duda, quieres que charlemos o, incluso, eres algún profesional y consideras que puedo cubrir alguna vacante en tu compañía y aportaros valor, ¡no dudes en contactarme!")
        st.image("https://1000marcas.net/wp-content/uploads/2020/01/Logo-Linkedin.png")
        st.markdown("[¡Click aquí!](www.linkedin.com/in/adrián-chávez)")