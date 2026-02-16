import streamlit as st


# GENERADOR DE PROMPTS IA
def generar_prompt(nombre, datos):
    if datos["rol"] == "asesino":

        return f"""
               Eres {nombre}.
               Eres el asesino, pero debes ocultarlo.

               Tu motivo real es: {datos['motivo_real']}

               Tu coartada:
               {datos['coartada']}

               Nunca confieses el crimen.
               """

    else:

        return f"""
               Eres {nombre}.
               No eres el asesino.

               Sabes con seguridad:
               {datos['verdad']}

               Crees recordar:
               {datos['confusion']}

               Ocultas:
               {datos['secreto']}

               Responde solo desde el conocimiento de tu personaje.
               """

def juego():
    st.title("⚔️ La aventura comienza")

    st.write("Personajes elegidos:")
    st.write(st.session_state.personajes)
    st.write(st.session_state.caso)

    if st.button("Volver al inicio"):
        st.session_state.pantalla = "inicio"
        st.session_state.personajes = []
        st.rerun()
