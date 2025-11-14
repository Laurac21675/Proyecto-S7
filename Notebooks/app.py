import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('/Users/laurarodriguez/Documents/Proyecto-S7/Proyecto-S7/vehicles_us.csv') # leer los datos
st.header('Analisis de venta de vehiculos')
hist_button = st.button('Construir histograma de kilometraje') # crear un botón
     
if hist_button: # al hacer clic en el botón
        
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#build_lineplot = st.checkbox('Construir evolucion precio promedio por dia')

#if build_lineplot: # si la casilla de verificación está seleccionada
#st.write('evolucion precio promedio segun condicion del vehiculo')
#df=car_data.groupby(['date_posted','condition'])['price'].mean().reset_index()



        