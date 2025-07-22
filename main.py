def soma():
    try:
        num1 = int(input("Introduza o primeiro número: "))
        num2 = int(input("Introduza o segundo número: "))

        soma = num1 + num2
        
        print(f"O resultado da soma é: {soma}")
    except ValueError:
        print("Os números devem ser inteiros")
        
def subtracao():
    try:
        num1 = int(input("Introduza o primeiro número: "))
        num2 = int(input("Introduza o segundo número: "))
        
        sub = num1 - num2
        
        print(f"O resultado da subtração é: {sub}")
    except ValueError:
        print("Os números devem ser inteiros")
        
def multiplicacao():
    try:
        num1 = int(input("Introduza o primeiro número: "))
        num2 = int(input("Introduza o segundo número: "))
        
        multi = num1 * num2
        print(f"O resultado da subtração é: {multi}")
    except ValueError:
        print("Os números devem ser inteiros")
        
def divisao():
    try:
        num1 = float(input("Introduza o primeiro número: "))
        num2 = float(input("Introduza o segundo número: "))
        
        if num1 > 0 and num2 > 0:
            div = num1 / num2
            print(f"O resultado da subtração é: {div}")
        else:
            print("è impossível dividir por 0.")
        
    except ValueError:
        print("Os números devem ser reais!")        

    except ZeroDivisionError:
        print("Erro! É impossível dividir por 0!")
        


while True:    
        
    print("\n Iniciando calculadora \n")
    print("1 - Somar números reais \n")
    print("2 - subtrair números reais \n")
    print("3 - multiplicar números reais \n")
    print("4 - dividir números reais \n")
    print("5 - finalizar programa \n")
    opcao = input("Indique a opção a executar: ")
        
    if opcao == "1":
        print("A executar a soma: ")
        soma()    
    elif opcao == "2":
        print("A executar a subtração: ")
        subtracao()
    elif opcao == "3":
        print("Ã executar a multiplicação: ")
        multiplicacao()    
    elif opcao == "4":
        print("A executar a divisão: ")
        divisao()
    elif opcao == "5":
        print("Obrigado! ")
        break
    else:
        print("Opção inválida! Tente novamente! ")