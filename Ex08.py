'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais.'''

l = [300, 25]
consumo_medio = l[0] / l[1]
print(f"Distância percorrida: {l[0]} km \nCombustível gasto: {l[1]} litros \nConsumo médio: {consumo_medio:.2f} km/l")
