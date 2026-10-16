
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não ´e possível dividir por zero.")

    return x / y

def potencia(x, y):
    return x ** y

# bloco principal para chamadas das funçẽos
def main():
    historico = []

    while True:
        print('\n===== CALCULADORA PYTHON ======')
        print('1. Adição')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Potência')
        print('6. Histórico')
        print('0. Sair')

        opcao = input('Por favor, digte uma opção: ')

        if opcao == '0':
            print('calculadora encerrado.')
            break
        
        if opcao == '6':
            if not historico:
                print('ainda não existem operações.')
            else:
                print('\n====== HISTÓRICO =========')

                for operacao in historico:
                    print(operacao)
                    continue

                    operacao = {
                            '1': ('Adição', adicionar, '+'),
                            '2': ('Subtração', subtrair, '-'),
                            '3': ('Multiplicação', multiplicar, '*'),
                            '4': ('Divisão', dividir, '/'),
                            '5': ('Potenciação', potencia, '**'),
                    }

                    if opcao not in operacao:
                        print('Opção inválida. Tenta novamente.')
                        continue
                
                try:
                    
                    x = float(input('Introduz o primeiro número: '))
                    y = float(input('Introduz o segundo número: '))

                    nome, funcao, simbolo = operacao[opcao]
                    resultado = funcao(x, y)

                    mensagem = f'{x} {simbolo} {y} = {resultado}'
                    print(f'resultado: {resultado}')

                    historico.append(mensagem)

                except ValueError as erro:
                    print(f'Erro: {erro}')

if  __name__ == "__main__":
    main()