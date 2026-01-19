quantidade = int(input("Quantos alunos? "))
soma = 0

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    soma = soma + nota

media = soma / quantidade
print("Média da turma:", media)
