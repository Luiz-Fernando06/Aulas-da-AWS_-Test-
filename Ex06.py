'''6- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

preco = 50
porcent = preco * 0.2
produto = "Camiseta"
desconto = preco - porcent
print(f'Produto: {produto} \nPreço unitário: {preco:.2f}R$ \nDesconto: {porcent:.0f}% \nPreço com desconto: {desconto:.2f}R$')
