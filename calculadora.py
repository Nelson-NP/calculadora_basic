
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError('Não é possível dividir por zero.')

    return a / b

def potencia(a, b):
    return a ** b

# Função main
def main():
    historico = []

    while True:
        print("\n===== CALCULADORA PYTHON =====")
        print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
        print("5 - Potênciação\n6 - Histórico\n0 - Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "0":
            print("Calculadora encerrada")
            break;

        if opcao == "6":
            if not historico:
                print("Ainda não existem operações.")
            else:
                print("\n====== HISTÕRICO =====")

                for operacao in historico:
                    print(operacao)
            continue
        
        operacoes = {
            "1":("Adição", adicionar, "+"),
            "2":("subtração", subtrair, "-"),
            "3":("Multiplicação", multiplicar, "*"),
            "4":("Divisão", dividir, "/"),
            "5":("Potenciação", potencia, "**"),
        }
        # Falta melhora está parte fazendo que quando clicarem 6 mostra info correto
        if opcao not in operacoes:
            print("Opção inválida. Tenta novamente.")
            continue
        # Aqui são pedido os valores da entrada
        try:
            a = float(input("Introduz o primeiro número: "))
            b = float(input("Introduz o segundo número: "))

            nome, funcao, simbolo = operacoes[opcao]
            resultado = funcao(a, b)

            mensagem = f"{a} {simbolo} {b} = {resultado}"

            print(f"Resultado: {resultado}")

            historico.append(mensagem)

        except ValueError as erro:
            print(f"Erro: {erro}")
            
# chamada da função main 
if __name__ == "__main__":
    main()
