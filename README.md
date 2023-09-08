# 1. Problema de Negócio

A empresa Zomato é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Zomato, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O problema de negócio da Zomato é a necessidade de compreender a fundo sua operação e os padrões de comportamento dos restaurantes cadastrados em sua plataforma. A empresa vem experimentando um crescimento significativo, o que trouxe a necessidade de otimizar processos internos. Com esse crescimento, os funcionários da empresa estão ficando presos em planilhas, realizando cálculos manualmente, o que consome tempo valioso e reduz a eficiência operacional. 

O CEO recém-contratado, assumiu o cargo em um momento crucial para a empresa. Ele traz consigo a visão de alavancar ainda mais a Zomato, mas para atingir esse objetivo, ele precisa compreender profundamente o negócio. No entanto, um desafio significativo se apresenta: a decisão de negócio é atrasada devido ao excesso de trabalho para a consolidação dos números da companhia, impossibilitando ações mais rápidas.

O CEO reconhece que, para direcionar a Zomato rumo ao sucesso contínuo, ele precisa de uma solução que lhe permita entender melhor a empresa, identificar áreas de oportunidade, aprimorar a experiência do cliente e tomar decisões ágeis e precisas. Portanto, é imperativo que seja realizada uma análise aprofundada nos dados da empresa e que sejam desenvolvidos dashboards que ofereçam a ele uma visão clara e em tempo real das informações necessárias para cumprir essa missão de forma eficaz.

# 2. Premissas do Negócio

1. Os dados utilizados nesta análise pode ser encontrados aqui
2. O Marketplace foi o modelo de negócio assumido para análise
3. O Dólar foi a moeda utilizada como padrão.
4. A conversão das moedas foram feitas com base na cotação do dia 01/07/2019

# 3. Estratégia da Solução

A estratégia para resolver o problema de negócio envolve as seguintes etapas:

1. Coleta de dados: Coletar e consolidar dados internos relevantes, como informações dos restaurantes, transações e avaliações.
2. Responder às perguntas do CEO: Utilizando um arquivo .pynb para explorar os dados ao mesmo tempo respondia as perguntas feitas pelo CEO.
3. Desenvolvimento de Dashboards: Criar dashboards utilizando o Streamlit que permite ao CEO visualizar rapidamente informações cruciais para tomar decisões informadas.

# 4. Top 3 Insights de dados

1. Por ser uma empresa que iniciou suas atividades na Índia, o país se destaca por obter o maior número de restaurantes na base de dados.
2. Apesar de ter grande parte dos restaurantes concentrados na Índia, o país não tem diversidades de tipos de culinárias.
3. Ter uma média de preço no prato para duas pessoas não está relacionado com maiores médias

# 5. O produto final do projeto

Dashboard online, hospedado em Cloud e disponível para acesso em qualquer dispositivo conectado a internet.

O painel pode ser acessado através do link: https://zomato-company-brazil.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibem essa métricas da melhor forma possível para o CEO.

O objetivo inicial foi completado, além disso, filtros foram adicionados no dashboard, afim de tirar insights com uma base de comparação mais ajustada, seleciando os países em que estão os restaurantes, ou até mesmo, na Visão Tipos de Culinárias, selecianando os tipos de culinárias.

Há espaço para melhorar o dashboard com análises mais complexas e que ofereçam 

# 7. Próximos Passos

1. Criar um ETL com a API do aplicativo
2. Melhorar a visualização das análise
3. Criação de novos filtros


Adicionar um ícone no sidebar para o download dos dados tratados.
