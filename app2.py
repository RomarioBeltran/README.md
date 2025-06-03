import pandas as pd
import plotly.express as px
import streamlit as st


# Título de la app
st.header("Análisis Exploratorio de Datos de Vehículos")

# Cargar el dataset
df = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma del odómetro')

if build_histogram:
    st.write('Creando un histograma para la columna odómetro')
    fig_hist = px.histogram(df, x='odometer', title='Distribución del kilometraje de los autos')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión: Precio vs. Año')

if build_scatter:
    st.write('Creando un gráfico de dispersión: Precio vs. Año del modelo')
    fig_scatter = px.scatter(df, x='model_year', y='price', color='condition',
                             title='Precio de autos vs. Año del modelo')
    st.plotly_chart(fig_scatter, use_container_width=True)

