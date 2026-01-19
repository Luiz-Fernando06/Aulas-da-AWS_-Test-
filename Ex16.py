pares = 0
impares = 0

quantidade = int(input("Quantos números serão digitados? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
