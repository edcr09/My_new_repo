import pandas as pd
import plotly_express as px
import streamlit as st

st.header('Gráficos de venta de vehiculos 2018 - 2019')

# Leer conjuntos de datos en los DataFrames

vehicles_us = pd.read_csv('C:/Users/Dell/Python_projects/Sprint_4/vehicles_us.csv' )

# Mostrar información del DataFrame

vehicles_us.info()
print(''' \n    
\n ''')
vehicles_us.describe()

# Mostrar informacion de columnas de datos tipo objeto (strings)

vehicles_us.describe(include=[object])

# Observaciones:

#Hay columnas con datos nulos y algunos tipos de valores pueden mejorar como:
#- model_year a int
#- date_posted a datetime
#- is_4wd a bool

# Histograma con plotly_express
hist_odom = px.histogram(vehicles_us, x="odometer") # crear un histograma
# hist_odom.show() 


# Grafico de dispersion
fig = px.scatter(vehicles_us, x="odometer", y="price") # crear un gráfico de dispersión
# fig.show() 

# Utilizando streamlit para generar checkbox

hist_chckbx = st.checkbox('Construir un histograma') #Crea checkbox de histograma

if hist_chckbx: # al hacer clic en el checkbox de histograma
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig_hist_chck = px.histogram(vehicles_us, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_hist_chck, use_container_width=True)


scat_chckbx = st.checkbox('Construir un grafico de dispersion') # Crea checkbox de grafico de dispersion

if scat_chckbx: # al seleccionar el checkbox de grafico de dispersion
            # escribir un mensaje
            st.write('Crear grafico de dispersion para el conjunto de datos de anuncios de venta de vehiculos')
            
            # crear un grafico de dispersion
            fig_sct_chck = px.scatter(vehicles_us, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_sct_chck, use_container_width=True)




