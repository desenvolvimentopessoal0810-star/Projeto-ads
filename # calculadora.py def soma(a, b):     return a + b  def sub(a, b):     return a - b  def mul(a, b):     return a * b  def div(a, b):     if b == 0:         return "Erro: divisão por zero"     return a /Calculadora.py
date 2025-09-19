# calculadora.py
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    print("=== Calculadora simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

if __name__ == "__main__":
    while True:
        menu()
        opc = input("Escolha operação: ")
        if opc == "0":
            break
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except:
            print("Entrada inválida. Tente novamente.")
            continue

        if opc == "1":
            print("Resultado:", soma(a,b))
        elif opc == "2":
            print("Resultado:", sub(a,b))
        elif opc == "3":
            print("Resultado:", mul(a,b))
        elif opc == "4":
            print("Resultado:", div(a,b))
        else:
            print("Opção inválida.")
        input("Pressione Enter para continuar...")
