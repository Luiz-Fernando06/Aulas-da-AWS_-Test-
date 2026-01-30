import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    dados = response.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except requests.exceptions.RequestException:
    print("Erro ao consultar o CEP.")
