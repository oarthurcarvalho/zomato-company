import pandas as pd
import streamlit as st
import inflection
import folium as fl
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from utils.data_cleaning import clean_data
from utils.helpers import country_name, create_price_type
from PIL import Image

#=====================================================================#
#               INÍCIO DA ESTRUTURA LÓGICA DO CÓDIGO                  #
#=====================================================================#

# ----------------- Importando o DataFrame ----------------- #
df = pd.read_csv('data/zomato.csv')
df1 = clean_data( df )


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


st.sidebar.markdown('### Dados Tratados')
st.sidebar.download_button('Baixe os Dados', data=df1.to_csv().encode('utf-8'), file_name='output.csv')


# ----------------- Página ----------------- #

st.markdown('<h1>Zomato!</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 25px;">O Melhor lugar para encontrar seu mais novo restaurante favorito!</p>', unsafe_allow_html=True)
st.markdown('<p>Temos as seguintes marcas dentro da nossa plataforma:</p>', unsafe_allow_html=True)

with st.container():

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        qnt_restaurantes = df1['restaurant_name'].count()
        qnt_restaurantes_format = f'{qnt_restaurantes:,}'.replace(',', '.')
        st.metric(label="Restaurantes Cadastrados", value=qnt_restaurantes_format)

    with col2:
        qnt_paises = df1['country_code'].nunique()
        
        st.metric(label="Países Cadastrados", value=qnt_paises)

    with col3:
        qnt_cidades = df1['city'].nunique()
        
        st.metric(label="Cidades Cadastradas", value=qnt_cidades)

    with col4:
        qnt_avaliacoes = df1['votes'].sum()
        qnt_avaliacoes_format = f'{qnt_avaliacoes:,}'.replace(',', '.')
        st.metric(label="Avaliações realizadas na Plataforma", value=qnt_avaliacoes_format)
        
    with col5:
        qnt_tipo_culinaria = df1['cuisines'].nunique()
        
        st.metric(label="Quantidade de Culinárias Oferecidas", value=qnt_tipo_culinaria)
        
with st.container():
    if df1.shape[0] != 0:
        
        geo_pos = df1[['latitude', 'longitude']]
        geo_media = [df1['latitude'].mean(), df1['longitude'].mean()]
        
        map = fl.Map(location=geo_media, zoom_start=2)
        MarkerCluster(locations=geo_pos).add_to(map)
        
    else:
        map = fl.Map(location=['21.98', '30.99'], zoom_start=2)
    
    folium_static( map, width=1420, height=520 )

















