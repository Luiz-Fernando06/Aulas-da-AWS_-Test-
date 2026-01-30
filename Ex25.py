import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    if "tempo_execucao" not in df.columns:
        print("Erro: A coluna 'tempo_execucao' não existe no arquivo.")
    else:
        media = df["tempo_execucao"].mean()
        desvio = df["tempo_execucao"].std()

        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")

except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
