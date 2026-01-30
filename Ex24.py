import requests

moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    dados = response.json()

    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]
        print("Valor atual:", info["bid"])
        print("Máxima:", info["high"])
        print("Mínima:", info["low"])
        print("Última atualização:", info["create_date"])

except requests.exceptions.RequestException:
    print("Erro ao consultar a moeda.")
