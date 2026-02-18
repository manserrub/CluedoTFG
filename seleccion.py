import streamlit as st
import random

def seleccion():

    st.title("🔍 Selecciona tus personajes")

    personajes = [
        "Coronel Mustard",
        "Profesor Plum",
        "Señora Peacock",
        "Señor Green",
        "Miss Scarlet",
        "Señora White"
    ]

    victimas = [
        "Señor Black",
        "Doctora Raven",
        "Barón Ashford",
        "Lady Crowley",
        "Profesor Hawthorne"
    ]

    armas = [
        "Cuchillo",
        "Candelabro",
        "Pistola",
        "Veneno",
        "Llave inglesa",
        "Cuerda",
        "Tijeras",
        "Martillo",
        "Baston"
    ]

    lugares = [
        "Biblioteca",
        "Cocina",
        "Comedor",
        "Salón",
        "Estudio",
        "Invernadero",
        "Baño",
        "Jardín",
        "Sotano"
    ]

    motivos = [
        "Celos",
        "Dinero",
        "Venganza",
        "Secreto descubierto",
        "Herencia",
        "Envidia"
    ]

    #Añadir secretos
    secretos = [
        "Estabas en un lugar donde no debías estar",
        "Tenías deudas con la víctima",
        "Discutiste con la víctima días antes",
        "Buscabas documentos privados",
        "Querías ocultar algo personal",
    ]

    horas = [
        "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:00", "00:00", "00:30"
    ]

    # FUNCIONES GENERADORAS
    def elegir_aleatorio(lista):
        return random.choice(lista)

    def generar_solucion():

        #Añadir un if para que la victima y los personajes sean parte de la seleccion
        victima = elegir_aleatorio(victimas)
        asesino = elegir_aleatorio(seleccion)

        return {
            "victima": victima,
            "asesino": asesino,
            "arma": elegir_aleatorio(armas),
            "lugar": elegir_aleatorio(lugares),
            "hora": elegir_aleatorio(horas),
            "motivo": elegir_aleatorio(motivos)
        }

    # GENERADOR DE PISTAS VERDADERAS .
    def pista_verdadera(solucion):

        tipo = random.choice(["arma", "lugar", "tiempo", "motivo"])

        if tipo == "arma":
            return f"Viste a alguien manipulando el arma {solucion['arma']} cerca de {solucion['victima']}"

        elif tipo == "lugar":
            return f"Oíste un ruido en {solucion['lugar']} donde apareció el cuerpo de {solucion['victima']}"

        elif tipo == "tiempo":
            return f"Recuerdas haber visto a {solucion['victima']} poco antes de las {solucion['hora']}"

        elif tipo == "motivo":
            return f"Sabes que alguien tenía un conflicto con {solucion['victima']} relacionado con {solucion['motivo']}"
        else:
            return ""

    # GENERADOR DE PISTAS FALSAS
    def pista_falsa(solucion):
        tipo = random.choice(["persona", "lugar", "hora"])

        if tipo == "persona":
            sospechoso = elegir_aleatorio(seleccion)
            return f"Crees que el culpable podría ser {sospechoso}"

        if tipo == "lugar":
            lugar = elegir_aleatorio(lugares)
            return f"Crees que el asesinato ocurrió en {lugar}"

        if tipo == "hora":
            hora = elegir_aleatorio(horas)
            return f"Crees que el crimen ocurrió alrededor de las {hora}"
        else:
            return ""

    # GENERAR PERSONAJES
    def generar_personajes(solucion):

        datos_personajes = {}

        for personaje in seleccion:

            if personaje == solucion["asesino"]:

                datos_personajes[personaje] = {
                    "rol": "asesino",
                    "coartada": f"Aseguras que estabas en {elegir_aleatorio(lugares)} a las {elegir_aleatorio(horas)}",
                    "motivo_real": solucion["motivo"]
                }

            else:
                datos_personajes[personaje] = {
                    "rol": "inocente",
                    "verdad": pista_verdadera(solucion),
                    "confusion": pista_falsa(solucion),
                    "secreto": elegir_aleatorio(secretos)
                }

        return datos_personajes

    # GENERADOR DEL MISTERIO
    def generar_misterio():

        solucion = generar_solucion()
        personajes_data = generar_personajes(solucion)

        return solucion, personajes_data

    seleccion = st.multiselect(
        "Elige tus personajes",
        personajes
    )

    if st.button("Comenzar partida"):

        if len(seleccion) == 0:
            st.error("Debes elegir al menos un personaje")
        else:
            st.session_state.caso, st.session_state.personajes = generar_misterio()
            st.session_state.pantalla = "juego"
            st.rerun()