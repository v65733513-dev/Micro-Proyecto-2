import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

ruta = "data\mascotas_limpio.csv"
df = pd.read_csv(ruta)

#---Background
st.image("https://github.com/v65733513-dev/Micro-Proyecto-2/raw/refs/heads/main/plantilla-banner-animal-lindos-felices-perros-gatos-espacio-text.avif",use_container_width=True)

#----Título de la aplicación---
st.title("Análisis de datos de Mascotas")

#----Bloque 1-----------------
seleccion_multiple1 = st.sidebar.multiselect(
    "Selecciona el tipo de especie de mascota:",
    df["especie"].unique()
)

##----Filtrado de datos
if seleccion_multiple1:
    df_filtrado1 = df[df["especie"].isin(seleccion_multiple1)]
else:
    df_filtrado1 = df

if st.checkbox("Mostar tabla de datos especies selleccionados"):
    st.write(df_filtrado1)

##----Gráfico de barras 
if not df_filtrado1.empty:
    conteo = df_filtrado1["especie"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(conteo.index, conteo.values, color = "#8CC0EB")
    ax.set_xlabel("Especie")
    ax.set_ylabel("Cantidad")
    ax.set_title("Cantidad de mascotas por especie")
    st.pyplot(fig)
else:
    st.warning("No hay datos para las especies seleccionadas")
    
st.divider()
#----Bloque 2---------------------------
seleccion_unica1 = st.sidebar.radio(
    "Selecciona el tipo de especie de mascota:",
    df["especie"].unique()
)

#----Bloque 3------------------------
seleccion_unica2 = st.sidebar.selectbox(
    "Selecciona el tipo de especie de mascota:",
    df["especie"].unique()
)
