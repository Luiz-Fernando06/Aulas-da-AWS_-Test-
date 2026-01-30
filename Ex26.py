arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

dados = [
    ("Nome", "Idade", "Cidade"),
    ("Ana", 25, "São Paulo"),
    ("Carlos", 30, "Rio de Janeiro"),
    ("Mariana", 22, "Belo Horizonte")
]

try:
    with open(arquivo, "w", encoding="utf-8") as f:
        for linha in dados:
            f.write(f"{linha[0]:<10}\t{linha[1]:<5}\t{linha[2]}\n")

    print("Arquivo salvo com sucesso.")

except Exception:
    print("Falha ao salvar o arquivo.")
