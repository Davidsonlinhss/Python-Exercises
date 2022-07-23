''' Exercício 4.8 - Escreva um programa que leia dois números e que pergunte qua operação você deseja realizar. Você deve
poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
'''

# Entrada de dados do usuário:
num1 = input('Digite o primeiro número:\n')
num2 = input('Digite o segundo número:\n')
ope = input('Qual operação você deseja realizar (+), (-), (*) ou (/)?\n')


# Condicionais e cálculos
if num1.isdigit() and num2.isdigit() and ope == '+':
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2  # Soma
    print(f' {num1} mais {num2} é igual a {soma}.')

elif num1.isdigit() and num2.isdigit() and ope == '-':
    num1 = int(num1)
    num2 = int(num2)
    subtração = num1 - num2  # Subtração
    print(f'{num1} menos {num2} é igual a {subtração}.')

elif num1.isdigit() and num2.isdigit() and ope == '*':
    num1 = int(num1)
    num2 = int(num2)
    multi = num1 * num2  # Multiplicação
    print(f'{num1} vezes {num2} é igual a {multi}')

elif num1.isdigit() and num2.isdigit() and ope == '/':
    num1 = int(num1)
    num2 = int(num2)
    divi = num1 / num2  # Divisão
    print(f'{num1} divido por {num2} é igual a {divi}.')

# Verificador das entradas fornecedias pelo usuário
else:
    message1 = 'não me parece válido para realizar uma operação'  # Frases
    message2 = 'não me parece válido para realizar uma operação de'
    if not num1.isdigit() and not num2.isdigit() and ope == '+':
        print(f'{num1} e {num2} {message2} soma.')

    elif not num1.isdigit() and not num2.isdigit() and ope == '-':
        print(f'{num1} e {num2} {message2} subtração.')

    elif not num1.isdigit() and not num2.isdigit() and ope == '*':
        print(f'{num1} e {num2} {message2} multiplicação.')

    elif not num1.isdigit() and not num2.isdigit() and ope == '/':
        print(f'{num1} e {num2} {message2} divisão.')
    else:
        if ope != '+,-,*,/':
            print(f'Digite uma operação válida, {ope} {message1} matemática.')