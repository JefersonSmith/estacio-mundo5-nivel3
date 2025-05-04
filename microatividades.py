import pandas as pd

arquivo_csv = './dados_atividade.csv'

print("--- Microatividade 1: Lendo o arquivo CSV ---")

df_original = pd.read_csv(arquivo_csv, sep=';', engine='python', quotechar='\'')
print("DataFrame Original Lido:")
print(df_original)
print("\n" + "-"*50 + "\n")

print("--- Microatividade 2: Criando um subconjunto de dados ---")
df_subconjunto = df_original[['Duration', 'Pulse', 'Calories']].copy()
print("Subconjunto de Dados (Duration, Pulse, Calories):")
print(df_subconjunto)
print("\n" + "-"*50 + "\n")

print("--- Microatividade 3: Configurando max_rows e exibindo com to_string() ---")
pd.options.display.max_rows = 9999
print("DataFrame Original Completo (com max_rows=9999):")
print(df_original.to_string())
print("\n" + "-"*50 + "\n")

pd.options.display.max_rows = 60

print("--- Microatividade 4: Exibindo as primeiras e últimas 10 linhas ---")
print("Primeiras 10 linhas:")
print(df_original.head(10))
print("\nÚltimas 10 linhas:")
print(df_original.tail(10))
print("\n" + "-"*50 + "\n")

print("--- Microatividade 5: Exibindo informações gerais (info()) ---")
print("Informações Gerais do DataFrame Original:")
df_original.info()
print("\n" + "-"*50 + "\n")

print("Microatividades concluídas.")

