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

linhas_selecionadas = df1['country'].isin( country_option )
df1 = df1.loc[linhas_selecionadas, : ].reset_index(drop=True)

if country_option:
    linhas_selecionadas = df1['country'].isin(country_option)
    df1 = df1.loc[linhas_selecionadas, :].reset_index(drop=True)
else:
    df1 = df1.head(0)
    st.sidebar.warning("Por favor, selecione pelo menos um país.")

num_cuisines = st.sidebar.slider(label="Selecione a quantidade de Restaurantes", min_value=5, max_value=15, value=5)

cuisines_list_default = df1.groupby('cuisines')['votes'].sum().sort_values(ascending=False).reset_index().loc[0:6, :]['cuisines']
cuisines_option = st.sidebar.multiselect(
    label="Escolha os Tipos de Culinária",
    options=df1['cuisines'].unique(), default=cuisines_list_default )

linhas_selecionadas = df1['cuisines'].isin( cuisines_option )
df1 = df1.loc[linhas_selecionadas, : ].reset_index(drop=True)

if cuisines_option:
    linhas_selecionadas = df1['cuisines'].isin(cuisines_option)
    df1 = df1.loc[linhas_selecionadas, :].reset_index(drop=True)
else:
    df1 = df1.head(0)
    st.sidebar.warning("Por favor, selecione pelo menos um país.")

# ----------------- Página ----------------- #
st.markdown('<h1 style="text-align: center;">Visão Tipos de Cozinhas</h1>', unsafe_allow_html=True)

with st.container():

    df_aux = ( df1.groupby('cuisines')['aggregate_rating']
              .mean()
              .round(2)
              .nlargest(5)
              .reset_index()
         ).cuisines

    df_filtrado = df1[df1['cuisines'].isin(df_aux)]
    colunas = ['aggregate_rating', 'restaurant_name', 'cuisines']
    df_result = ( df_filtrado.groupby('cuisines')[colunas]
                             .agg({
                                 'aggregate_rating': 'max',
                                 'restaurant_name': 'first',
                                 'cuisines': 'first'})
                             .reset_index(drop=True)
                )
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        info = df_result.loc[0, :]
        st.metric(label=f"{info['cuisines']}: {info['restaurant_name']}", value=f"{info['aggregate_rating']}/5.0")
    with col2:
        info = df_result.loc[1, :]
        st.metric(label=f"{info['cuisines']}: {info['restaurant_name']}", value=f"{info['aggregate_rating']}/5.0")
    with col3:
        info = df_result.loc[2, :]
        st.metric(label=f"{info['cuisines']}: {info['restaurant_name']}", value=f"{info['aggregate_rating']}/5.0")
    with col4:
        info = df_result.loc[3, :]
        st.metric(label=f"{info['cuisines']}: {info['restaurant_name']}", value=f"{info['aggregate_rating']}/5.0")
    with col5:
        info = df_result.loc[4, :]
        st.metric(label=f"{info['cuisines']}: {info['restaurant_name']}", value=f"{info['aggregate_rating']}/5.0")

with st.container():
    colunas = ['restaurant_id', 'restaurant_name', 'country',
           'city', 'cuisines', 'average_cost_for_two_usd',
           'aggregate_rating', 'votes']

    df_aux = ( df1.loc[:, colunas]
                  .sort_values(['aggregate_rating', 'votes'], ascending=False)
                  .reset_index(drop=True)
                  .loc[0:num_cuisines-1, :]
             )
    st.dataframe( df_aux, use_container_width=True )
    
with st.container():
    col1, col2, = st.columns(2)
    df1 = get_processed_data('data/zomato.csv')
    with col1:
        
        df_aux = ( df1.groupby('cuisines')['aggregate_rating']
                  .mean()
                  .round(2)
                  .sort_values(ascending=False)
                  .reset_index()
                  .loc[0:7, :]
             )

        plot_bar_chart(df_aux, x='cuisines', y='aggregate_rating',
                       y_title="Média de Avaliação", 
                       x_title="Cidades", 
                       title='Top 7 Cidades com mais Restaurantes na Base de Dados',
                       text_col="aggregate_rating"
        )
        
    with col2:
        
        df_aux = ( df1.groupby('cuisines')['aggregate_rating']
                      .mean()
                      .round(2)
                      .sort_values(ascending=True)
                      .reset_index()
                      .loc[0:9, :]
                 )
        plot_bar_chart(df_aux, x='cuisines', y='aggregate_rating',
                       y_title="Média de Avaliação", 
                       x_title="Cidades", 
                       title='Top 7 Cidades com mais Restaurantes na Base de Dados',
                       text_col="aggregate_rating"
        )