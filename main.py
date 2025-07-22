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
    opcao = input("Indique a opção a executar: ")























#import os
#import time
#
#def calculadora(num1: float, num2: float, operador: str) -> float:
#    """
#    Usar nan como valor inicial é uma boa prática. 
#    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
#    sinalizando que o cálculo não pôde ser realizado.
#    """
#    result = float("nan")
#    if operador == '+':
#        result = num1 + num2
#
#    return result
#
#
#if __name__ == "__main__":
#
#    while True:
#        os.system('cls' if os.name == 'nt' else 'clear')
#        try:
#            print('Calculadora')
#            print('----------------------------------\n')
#
#
#        except ValueError:
#            print('Dados inválidos! -> Tente novamente!')
#            time.sleep(2)
#
#        except ZeroDivisionError:
#            print('Impossível dividir por zero! -> Tente novamente!')
#            time.sleep(2)
#
#    print('\nVolte sempre!\n')
#