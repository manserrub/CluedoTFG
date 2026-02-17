import streamlit as st
from openai import OpenAI

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



def conversacion(nombre,datos,caso):
    st.write(caso)
    st.write(generar_prompt(nombre,datos))

    client = OpenAI()

    PROMPT = generar_prompt(nombre,datos)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": PROMPT}
        ]

    # Mensaje inicial del sospechoso
    if len(st.session_state.messages) == 1:
        greeting = "🔍 Buenas señor detective ¿Qué necesita?"
        st.session_state.messages.append(
            {"role": "assistant", "content": greeting}
        )

    # MOSTRAR CHAT
    for msg in st.session_state.messages[1:]:  # ignorar system
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # INPUT USUARIO
    if prompt := st.chat_input("Escribe tu mensaje..."):

        # Mostrar mensaje usuario
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # RESPUESTA IA
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        with st.chat_message("assistant"):
            st.markdown(reply)


