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

st.markdown('<h1 style="text-align: center;">Visão Países</h1>', unsafe_allow_html=True)

with st.container():

    col1, col2 = st.columns(2)
    with col1:
        df_aux = ( df1.groupby('country_sigla')['restaurant_name']
                      .count()
                      .sort_values(ascending=False)
                      .reset_index()
                 )
        plot_bar_chart(df_aux, x='country_sigla', y='restaurant_name',
                       y_title="Quantidade de Restaurantes", 
                       x_title="Países", 
                       title='Quantidade de Restaurantes Registrados por País',
                       text_col="restaurant_name"
        )

    with col2:
        df_aux = df1.groupby('country_sigla')['city'].nunique().sort_values(ascending=False).reset_index()
        plot_bar_chart(df_aux, x='country_sigla', y='city',
                       y_title="Quantidade de Cidades", 
                       x_title="Países", 
                       title='Quantidade de Cidades Registrados por País',
                       text_col="city"
        )
        
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_aux = df1.groupby('country_sigla')['votes'].mean().round(2).sort_values(ascending=False).reset_index()

        plot_bar_chart(df_aux, x='country_sigla', y='votes',
               y_title="Avaliações Média", 
               x_title="Países", 
               title='Média de Avaliações feitas por País',
               text_col="votes"
        )

    with col2:
        df_aux = ( df1.groupby('country_sigla')['average_cost_for_two_usd']
                      .mean()
                      .round(2)
                      .sort_values(ascending=False)
                      .reset_index()
                 )
        plot_bar_chart(df_aux, x='country_sigla', y='average_cost_for_two_usd',
               y_title="Preço Médio (US$)", 
               x_title="Países", 
               title='Preço Médio Prato para duas pessoas por País',
               text_col="average_cost_for_two_usd"
        )