import streamlit as st
import random
import json

# Cargar el archivo JSON
def cargar_datos():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Función para mostrar el aparato y la canción aleatoria
def mostrar_aleatorio():
    datos = cargar_datos()
    seleccion = random.choice(datos)
    st.write(f"Aparato: {seleccion['aparato']}")
    st.write(f"Canción: {seleccion['cancion']}")

# Interfaz de la web
st.title("Aparato de Gimnasia Rítmica con Canción")
st.button("Mostrar Aleatorio", on_click=mostrar_aleatorio)
