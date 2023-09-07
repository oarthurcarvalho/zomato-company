import pandas as pd
import inflection
from utils.helpers import country_name, create_price_type, color_name

def country_name(country_id):
    """
    Retorna o nome do país com base em seu ID.

    Parâmetros:
        - country_id (int): O ID do país.

    Retorna:
        str: O nome do país correspondente ao ID.
    """
    COUNTRIES = {
        1: "India", 14: "Australia", 30: "Brazil", 37: "Canada",
        94: "Indonesia", 148: "New Zeland", 162: "Philippines",
        166: "Qatar", 184: "Singapure", 189: "South Africa",
        191: "Sri Lanka", 208: "Turkey", 214: "United Arab Emirates",
        215: "England", 216: "United States of America",
    }

    return COUNTRIES[country_id]

def color_name(color_code):
    """
    Retorna o nome da cor com base em seu código hexadecimal.

    Parâmetros:
        - color_code (str): O código hexadecimal da cor.

    Retorna:
        str: O nome da cor correspondente ao código.
    """
    COLORS = {
        "3F7E00": "darkgreen", "5BA829": "green",
        "9ACD32": "lightgreen", "CDD614": "orange",
        "FFBA00": "red", "CBCBC8": "darkred",
        "FF7800": "darkred"
    }
    
    return COLORS[color_code]

def rename_columns(dataframe):
    """
    Renomeia as colunas do dataframe para seguir convenções de estilo.

    Parâmetros:
        - dataframe (pd.DataFrame): O dataframe a ser renomeado.

    Retorna:
        pd.DataFrame: O dataframe com colunas renomeadas.
    """
    # Função para renomear as colunas do dataframe
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def convert_to_usd(df):
    """
    Converte os preços no dataframe para USD com base em uma taxa de câmbio.

    Parâmetros:
        - df (pd.DataFrame): O dataframe com os preços a serem convertidos.

    Retorna:
        pd.DataFrame: O dataframe com os preços convertidos para USD.
    """
    convert_dict = {
        'Botswana Pula(P)': 0.094, 'Brazilian Real(R$)': 3.78, 'Dollar($)': 1, 'Emirati Diram(AED)': 0.27223,
        'Indian Rupees(Rs.)': 0.014322, 'Indonesian Rupiah(IDR)': 0.00007097, 'NewZealand($)': 0.66765,
        'Pounds(£)': 1.2645, 'Qatari Rial(QR)': 0.2746, 'Rand(R)': 0.070731, 'Sri Lankan Rupee(LKR)': 0.0056453,
        'Turkish Lira(TL)': 0.17689
    }

    df['average_cost_for_two_usd'] = df.apply(
        lambda row: convert_dict[row['currency']] * row['average_cost_for_two'], axis=1)

    return df

def create_sigla( dataframe ):
    paises_sigla = {
        'Philippines': 'PHL', 'Brazil': 'BRA', 'Australia': 'AUS',
        'United States of America': 'USA', 'Canada': 'CAN',
        'Singapore': 'SGP', 'United Arab Emirates': 'ARE',
        'India': 'IND', 'Indonesia': 'IDN', 'New Zealand': 'NZL',
        'England': 'GBR', 'Qatar': 'QAT', 'South Africa': 'ZAF',
        'Sri Lanka': 'LKA', 'Turkey': 'TUR'
    }

    dataframe['country_sigla'] = dataframe['country'].map(paises_sigla)

    return dataframe

def remove_outliers(dataframe, column):
    """
    Remove outliers do dataframe com base em uma coluna específica.

    Parâmetros:
        - dataframe (pd.DataFrame): O dataframe a ser processado.
        - column (str): O nome da coluna usada para identificar outliers.

    Retorna:
        pd.DataFrame: O dataframe sem os outliers.
    """
    Q1 = dataframe[column].quantile(0.15)
    Q3 = dataframe[column].quantile(0.95)
    IQR = Q3 - Q1
    banda_inferior = Q1 - 1.5 * IQR
    banda_superior = Q3 + 1.5 * IQR
    df_sem_outlier = dataframe[~((dataframe[column] < banda_inferior) | (dataframe[column] > banda_superior))]
    return df_sem_outlier

def clean_data(dataframe):
    """
    Realiza a limpeza e transformação dos dados no dataframe.

    Parâmetros:
        - dataframe (pd.DataFrame): O dataframe a ser limpo.

    Retorna:
        pd.DataFrame: O dataframe limpo e transformado.
    """
    # Renomeando as colunas
    df1 = rename_columns( dataframe )
    
    # Removendo linhas
    df1.drop_duplicates(['restaurant_id'], keep='first', inplace=True)
    
    # Tagueando os países pelo código
    df1['country'] = df1['country_code'].apply(country_name)
    
    # Tagueado as cores de avaliações dos países
    df1['rating_color'] = df1['rating_color'].apply(color_name)
    
    # Categorizando a coluna de cuisines
    df1.loc[:, 'cuisines'] = df1["cuisines"].str.split(",").str[0]
    
    df1.drop(['switch_to_order_menu'], axis = 1, inplace=True)
    
    # Criando a coluna para converter as moedas em USD
    df1 = convert_to_usd( df1 )
    
    # Retirando os outliers da coluna average_cost_for_two_usd
    df1 = remove_outliers( df1, 'average_cost_for_two_usd')
    
    df1 = create_sigla( df1 )

    return df1.reset_index(drop=True)

def get_processed_data( csv_path ):

    df = pd.read_csv( csv_path )
    df1 = clean_data( df )

    return df1