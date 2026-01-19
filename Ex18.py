texto = input("Digite uma palavra ou frase: ")

texto_limpo = texto.replace(" ", "").lower()
texto_invertido = texto_limpo[::-1]

if texto_limpo == texto_invertido:
    print("Sim")
else:
    print("Não")
