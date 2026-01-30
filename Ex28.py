import json

arquivo = "dados_pessoas.json"

dados = {
    "pessoas": [
        {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Mariana", "idade": 22, "cidade": "Belo Horizonte"}
    ]
}

try:
    # Escrita do arquivo JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    # Leitura do arquivo JSON
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    for pessoa in dados_lidos["pessoas"]:
        print(
            f"Nome: {pessoa['nome']}, "
            f"Idade: {pessoa['idade']}, "
            f"Cidade: {pessoa['cidade']}"
        )

except FileNotFoundError:
    print("Erro: Arquivo JSON não encontrado.")
except Exception:
    print("Erro ao salvar ou ler o arquivo JSON.")
