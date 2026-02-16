import streamlit as st

def inicio():
    st.title("🎮 MI JUEGO")

    if st.button("Iniciar Juego"):
        st.session_state.pantalla = "seleccion"
        st.rerun()