'''
Primeira calculadora simples construída através da aula.
'''

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operator = input('Digite um operador: ')

# Verificador para os inputs numerais
    if not num_1.isnumeric() or not num_2.isnumeric():  # Estamos verificando se foi digitado um número válido
        print('Você precisa digitar um número válido.')  # Se não for digitado um numeral, ele imprime uma mensagem de erro e pula as funções de operação

        sair = input('Deseja sair? [s]sim ou [n]não:\n')  # Primeiro ponto de checagem caso seja digitado de forma incorreta os inputs
        if sair == 's':
            print('Até a próxima.')
            break
        elif sair == 'n':
            continue

# Funções operacionais básicas
    if operator == '+':
        num_1 = int(num_1)
        num_2 = int(num_2)
        print(num_1 + num_2)
    elif operator == '-':
        num_1 = int(num_1)
        num_2 = int(num_2)
        print(num_1 - num_2)
    elif operator == '*':
        num_1 = int(num_1)
        num_2 = int(num_2)
        print(num_1 * num_2)
    elif operator == '/':
        num_1 = int(num_1)
        num_2 = int(num_2)
        print(num_1 / num_2)
    else:
        print('Operador inválido.')

# Segundo ponto de checagem após a operação perguntando se o usuário deseja sair ou realizar outra operação
    sair = input('Deseja sair? [s]sim ou [n]não:\n')
    if sair == 's':
        print('Até a próxima.')
        break