
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def multiplicar(a, b):
    return a * b

def exponenciar(a, b):
    return a ** b


def mostrar_menu():
    print("""    1 - Somar
    2 - Subtrair
    3 - Divisão 
    4 - Multiplicação
    5 - Exponenciação """)
    
    opcao = int(input("Escolha uma operação: "))
    return opcao


def calculadora():
    while True:
        opcao = mostrar_menu()

        if opcao == 0:
            print("Encerrando...")
            break

        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))

        if opcao == 1:
            resultado = somar(num1, num2)
        elif opcao == 2:
            resultado = subtrair(num1, num2)
        elif opcao == 3:
            resultado = dividir(num1, num2)
        elif opcao == 4:
            resultado = multiplicar(num1, num2)
        elif opcao == 5:
            resultado = exponenciar(num1, num2)
        else:
            print("Opção inválida!")
            continue

        print(f"Resultado: {resultado}")

calculadora()
        