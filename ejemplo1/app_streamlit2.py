import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar saludos
saludos = session.query(Saludo2).all()

# Mostrar tabla con todos los datos
st.title("Presentación de todos los Saludos en Tabla")

lista = []
for s in saludos:
    diccionario = {
        "id": s.id,
        "mensaje": s.mensaje,
        "tipo": s.tipo,
        "origen": s.origen
    }
    lista.append(diccionario)

st.dataframe(lista)
