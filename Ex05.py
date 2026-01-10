'''5- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''


carteira = 100
dolar = carteira / 5.20
print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, dolar))
print('Com R${:.2f} você pode comprar E${:.2f}'.format(carteira, (carteira / 6.15)))
