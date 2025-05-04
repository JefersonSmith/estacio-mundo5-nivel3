import pandas as pd
import numpy as np

arquivo_csv = './dados_atividade.csv'

print("--- Missão Prática: Tratamento de Dados ---")

print("\nPasso 1: Lendo o arquivo CSV")
df_original = pd.read_csv(arquivo_csv, sep=';', engine='python', quotechar='\'')
print("DataFrame Original Lido:")
print(df_original)

print("\nPasso 2: Verificando a importação dos dados")
print("\nInformações gerais sobre o conjunto de dados:")
df_original.info()

print("\nPrimeiras 5 linhas do arquivo:")
print(df_original.head())

print("\nÚltimas 5 linhas do arquivo:")
print(df_original.tail())

print("\nPasso 3: Criando uma cópia do DataFrame original")
df_tratado = df_original.copy()
print("Cópia criada com sucesso.")

print("\nPasso 4: Substituindo valores nulos da coluna 'Calories' por 0")
df_tratado['Calories'] = df_tratado['Calories'].fillna(0)
print("DataFrame após substituição dos valores nulos em 'Calories':")
print(df_tratado)

print("\nPasso 5: Substituindo valores nulos da coluna 'Date' por '1900/01/01'")
df_tratado['Date'] = df_tratado['Date'].fillna('1900/01/01')
print("DataFrame após substituição dos valores nulos em 'Date':")
print(df_tratado)

print("\nPasso 6: Tentando transformar a coluna 'Date' em datetime")
try:
    df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], format='%Y/%m/%d')
    print("Conversão realizada com sucesso.")
except Exception as e:
    print(f"Erro na conversão: {e}")

print("\nPasso 7: Substituindo '1900/01/01' por NaN na coluna 'Date'")
df_tratado['Date'] = df_tratado['Date'].replace('1900/01/01', np.nan)
print("DataFrame após substituição de '1900/01/01' por NaN:")
print(df_tratado)

print("\nPasso 8: Tentando novamente transformar a coluna 'Date' em datetime")
try:
    df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], format='%Y/%m/%d')
    print("Conversão realizada com sucesso.")
except Exception as e:
    print(f"Erro na conversão: {e}")

print("\nPasso 9: Transformando o valor '20201226' para o formato datetime")
mask = df_tratado['Date'] == '20201226'
if mask.any():
    df_tratado.loc[mask, 'Date'] = pd.to_datetime('2020/12/26')
    print("Valor '20201226' transformado com sucesso.")
else:
    print("Valor '20201226' não encontrado.")

print("\nPasso 10: Executando a transformação final da coluna 'Date' para datetime")
try:
    df_tratado['Date'] = pd.to_datetime(df_tratado['Date'])
    print("Conversão final realizada com sucesso.")
    print("DataFrame após conversão final da coluna 'Date':")
    print(df_tratado)
except Exception as e:
    print(f"Erro na conversão final: {e}")

print("\nPasso 11: Removendo registros com valores nulos na coluna 'Date'")
df_tratado = df_tratado.dropna(subset=['Date'])
print("DataFrame após remoção de registros com valores nulos em 'Date':")
print(df_tratado)

print("\nPasso 12: Verificação final do DataFrame")
print("\nInformações gerais sobre o DataFrame tratado:")
df_tratado.info()

print("\nDataFrame tratado final:")
print(df_tratado)

print("\nMissão Prática concluída com sucesso!")
