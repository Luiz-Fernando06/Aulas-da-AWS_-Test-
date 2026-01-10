'''3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.'''
notas = [7.5, 8.0, 6.5]
m = sum(notas)/len(notas)
p = f"Nota 1: {notas[0]:.1f} \nNota 2: {notas[1]:.1f} \nNota 3: {notas[2]:.1f} \nMédia: {m:.1f}".replace(".",",")
print(p)


