import streamlit as st
from inicio import *
from juego import *
from seleccion import *

st.set_page_config(page_title="CLUEDO", page_icon='🔍',layout="wide",initial_sidebar_state="collapsed")

# Inicializar estado
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "caso" not in st.session_state:
    st.session_state.caso = []

if "personajes" not in st.session_state:
    st.session_state.personajes = []


# PANTALLA 1 - INICIO
if st.session_state.pantalla == "inicio":
    inicio()

# PANTALLA 2 - SELECCION PERSONAJES
elif st.session_state.pantalla == "seleccion":
    seleccion()

# PANTALLA 3 - JUEGO
elif st.session_state.pantalla == "juego":
    juego()