# helpers.py

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
    return COUNTRIES.get(country_id, "")

def create_price_type(price_range):
    """
    Cria e retorna o tipo de preço com base no intervalo de preços.

    Parâmetros:
        - price_range (int): O intervalo de preços (1, 2 ou 3).

    Retorna:
        str: O tipo de preço ("cheap", "normal", "expensive" ou "gourmet").
    """
    price_types = {1: "cheap", 2: "normal", 3: "expensive"}
    return price_types.get(price_range, "gourmet")

def color_name(color_code):
    # Função para obter o nome da cor a partir do código
    COLORS = {
        "3F7E00": "darkgreen", "5BA829": "green",
        "9ACD32": "lightgreen", "CDD614": "orange",
        "FFBA00": "red", "CBCBC8": "darkred",
        "FF7800": "darkred"
    }
    return COLORS.get(color_code, "")
