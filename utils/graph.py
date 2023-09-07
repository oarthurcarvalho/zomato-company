import plotly.express as px
import streamlit as st
import pandas as pd

def plot_bar_chart(data, x, y, y_title, x_title, title, text_col=None):
    """
    Plota um gráfico de barras.

    Parâmetros:
    - data (pd.DataFrame): O DataFrame contendo os dados.
    - x (str): A coluna do DataFrame para o eixo x.
    - y (str): A coluna do DataFrame para o eixo y.
    - y_title (str): Título do eixo y.
    - x_title (str): Título do eixo x.
    - title (str): Título do gráfico.
    - text_col (str, opcional): Coluna para adicionar rótulos nas barras.
    """
    fig = px.bar(data_frame=data, x=x, y=y, text=text_col)
    fig.update_yaxes(
            title = dict(
                font=dict(
                    size=18
                ),
                text=y_title
            )
        )
    fig.update_xaxes(
            title = dict(
                font=dict(
                    size=18
                ),
                text=x_title
            )
        )
    fig.update_layout(
        title=dict(text=title, font=dict(size=20, family="Arial"), x=0.5, xanchor="center")
    )

    if data.shape[0] == 0:
        fig.add_annotation(
            text="<b>Sem Dados</b>",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            textangle=-25,
            font=dict(family="Arial", size=40),
            opacity=0.3,
        )

    st.plotly_chart(fig, use_container_width=True)
