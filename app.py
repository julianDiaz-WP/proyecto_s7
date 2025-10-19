import pandas as pd
import plotly.express as px
import streamlit as st

st. header('Análisis de datos de venta de vehículos usados')

# leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# creación del checkbox para habilitar la creación del histograma
built_histogram = st.checkbox('Habilitar histograma')
# creación del botón para generar histograma
hist_button = st.button('Construir histograma')

if built_histogram and hist_button:  # al hacer clic en el botón
    # mensaje descriptivo
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de autos')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar el histograma interactivo con Plotly
    st.plotly_chart(fig, use_container_width=True)

# creación del checkbox para habilitar la creación del gráfico de dispersión
built_scatter = st.checkbox('Habilitar gráfico de dispersión')

# creación del botón para generar gráfico de dispersión
scatter_button = st.button('Construir gráfico de disperisón')

if built_scatter and scatter_button:  # al hacer clic en el botón
    # mensaje descriptivo
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de autos')

    # crear el gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')

    # mostrar el gráfico de dispersión interactivo con plotly
    st.plotly_chart(fig, use_container_width=True)
