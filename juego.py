import streamlit as st
from conversacion import *

def juego():
    st.title("🔍 El caso comienza")

    caso = st.session_state.caso
    menu = st.session_state.personajes

    choice = st.selectbox(f'**MENU**',menu)

    if choice == "Coronel Mustard":
        conversacion("Coronel Mustard",menu["Coronel Mustard"],caso)
    elif choice == "Profesor Plum":
        conversacion("Profesor Plum",menu["Profesor Plum"],caso)
    elif choice == "Señora Peacock":
        conversacion("Señora Peacock",menu["Señora Peacock"],caso)
    elif choice == "Señora White":
        conversacion("Señora White",menu["Señora White"],caso)
    elif choice == "Señor Green":
        conversacion("Señor Green",menu["Señor Green"],caso)
    elif choice == "Miss Scarlet":
        conversacion("Miss Scarlet",menu["Miss Scarlet"],caso)


    #st.write("Personajes elegidos:")
    #st.write(st.session_state.personajes)
    #st.write(st.session_state.caso)


    #if st.button("Volver al inicio"):
    #    st.session_state.pantalla = "inicio"
    #    st.session_state.personajes = []
    #    st.rerun()
