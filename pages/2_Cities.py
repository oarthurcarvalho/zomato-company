import pandas as pd
import streamlit as st
import inflection
import folium as fl
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import plotly.express as px
from utils.data_cleaning import get_processed_data
from utils.graph import plot_bar_chart
from PIL import Image

#=====================================================================#
#               INÍCIO DA ESTRUTURA LÓGICA DO CÓDIGO                  #
#=====================================================================#

# ----------------- Importando o DataFrame ----------------- #
df1 = get_processed_data('data/zomato.csv')

# ----------------- Configurando o Streamlit ----------------- #
st.set_page_config(
    page_title='Home - Zomato',
    page_icon='img/zomato-logo.png', layout='wide'
)

# ----------------- Barra Lateral ----------------- #

image_path = 'img/zomato-logo.png'
image = Image.open( image_path )
st.sidebar.image( image, width=200, use_column_width='always' )
st.sidebar.header("Filtros")

country_list_default = ( df1.groupby('country')['restaurant_id']
                            .nunique()
                            .sort_values(ascending=False)
                            .reset_index()
                            .iloc[0:6, 0]
                       )
country_option = st.sidebar.multiselect(
    label="Quais países você deseja visualizar os restaurantes",
    options=df1['country'].unique(), default=country_list_default )

if country_option:
    linhas_selecionadas = df1['country'].isin(country_option)
    df1 = df1.loc[linhas_selecionadas, :].reset_index(drop=True)
else:
    df1 = df1.head(0)
    st.sidebar.warning("Por favor, selecione pelo menos um país.")

# ----------------- Página ----------------- #

st.markdown('<h1 style="text-align: center;">Visão Cidades</h1>', unsafe_allow_html=True)

with st.container():

    df_aux = ( df1.groupby('city')['restaurant_name']
                      .count()
                      .sort_values(ascending=False)
                      .reset_index()
                      .loc[0:9, :]
                 )
    plot_bar_chart(df_aux, x='city', y='restaurant_name',
                       y_title="Quantidade de Restaurantes", 
                       x_title="Cidades", 
                       title='Top 10 Cidades com mais Restaurantes na Base de Dados',
                       text_col="restaurant_name"
    )
    
        
with st.container():

    col1, col2 = st.columns(2)

    with col1:
        df_select = df1.loc[df1['aggregate_rating'] >= 4]
        df_aux = df_select.groupby('city')['restaurant_name'].count().sort_values(ascending=False).reset_index().loc[0:6, :]
        plot_bar_chart(df_aux, x='city', y='restaurant_name',
                       y_title="Quantidade de Restaurantes", 
                       x_title="Cidades", 
                       title='Top 7 Cidades com mais Restaurante ótimos (< 4)',
                       text_col="restaurant_name"
        )
        
    with col2:
        df_select = df1.loc[df1['aggregate_rating'] <= 2.5]
        df_aux = df_select.groupby('city')['restaurant_name'].count().sort_values(ascending=False).reset_index().loc[0:6, :]
        plot_bar_chart(df_aux, x='city', y='restaurant_name',
               y_title="Quantidade de Restaurantes", 
               x_title="Cidades", 
               title='Top 7 Cidades com mais Restaurante ruins (> 2.5)',
               text_col="restaurant_name"
        )

with st.container():
    df_aux = df1.groupby('city')['cuisines'].nunique().sort_values(ascending=False).reset_index().loc[0:9, :]
    plot_bar_chart(df_aux, x='city', y='cuisines',
       y_title="Quantidade de Restaurantes", 
       x_title="Cidades", 
       title='Top 10 Cidades com Culinárias Distintos',
       text_col="cuisines"
    )