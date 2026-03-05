import pandas as pd

# Coisas Importantes - Passo a Passo
# 1. Abrir a base de dados.
# pip install pandas openpyxl nbformat ipykernel plotly

tabela = pd.read_csv("cancelamentos.csv")


# 2. Visualizar a base de dados.
    # entender as informações e observar erros
    # informações inúteis, não ajudam você.

tabela = tabela.drop(columns="CustomerID")
print(tabela)

# 3. Corrigir problemas da base de dados.
# 4. Análise inicial (entender quantos clientes cancelaram)
# 5. Análise detalhada
