tentativa = 0
max_tentativa = 3

while tentativa < max_tentativa:
    try:
        num1 = float(input("\nDigite um numero: "))
        num2 = float(input("\nDigite um numero: "))

        resultado = num1 / num2
        print("Resultado da divisão: ", resultado)
        break
    except ValueError:
        tentativa += 1
        print(f"\nErro: digite apenas numeros. Tentativas {tentativa}/3\n")


    except ZeroDivisionError:
        tentativa += 1
        print(f"\nErro: Não é possivel dividir por 0. Tentativas {tentativa}/3\n.")
    
    finally:
        if tentativa == max_tentativa:
            print("Numero max de tentativas atingido. Encerrando o programa")
