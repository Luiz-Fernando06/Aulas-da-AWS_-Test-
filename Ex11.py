temp = float(input("Digite a temperatura: "))
origem = input("Origem (C, F ou K): ")
destino = input("Destino (C, F ou K): ")

if origem == "C" and destino == "F":
    print((temp * 9/5) + 32)

elif origem == "C" and destino == "K":
    print(temp + 273.15)

elif origem == "F" and destino == "C":
    print((temp - 32) * 5/9)

elif origem == "F" and destino == "K":
    print((temp - 32) * 5/9 + 273.15)

elif origem == "K" and destino == "C":
    print(temp - 273.15)

elif origem == "K" and destino == "F":
    print((temp - 273.15) * 9/5 + 32)

else:
    print("Conversão inválida")
