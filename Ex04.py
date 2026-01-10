'''4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.'''

preco = 12.40
qtd = 3 
produto = "Cadeira Infantil"
print(f'Produto: {produto} \nPreço unitário: {preco:.2f} \nQuantidade {qtd} \nPreço Total: {preco*qtd:.2f}')
