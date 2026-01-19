def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


valor = float(input("Valor da conta: "))
porcentagem = float(input("Porcentagem da gorjeta: "))

resultado = calcular_gorjeta(valor, porcentagem)
print("Valor da gorjeta:", resultado)
