import pandas as pd
#ferramentas de visualização
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt


# Coisas Importantes - Passo a Passo
# 1. Abrir a base de dados.
# pip install pandas openpyxl nbformat ipykernel plotly

tabela = pd.read_csv("cancelamentos.csv")


# 2. Visualizar a base de dados.
    # entender as informações e observar erros
    # informações inúteis, não ajudam você. então, remova.

print(tabela.head())     # primeiras linhas
print(tabela.info())     # estrutura das colunas
print(tabela.describe()) # estatísticas básicas

# 3. Corrigir problemas da base de dados.

tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna() # em projetos maiores poderíamos preencher valores, mas aqui remover funciona bem

# 4. Análise inicial (entender quantos clientes cancelaram)

grafico = px.histogram(tabela, x="cancelou", color="cancelou")
grafico.show()

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", barmode="overlay")
    grafico.show()

correlacao = tabela.corr(numeric_only=True)
print(correlacao)

sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.show()    

print(tabela.groupby("cancelou").mean(numeric_only=True))

# 5. Análise detalhada
