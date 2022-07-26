'''
Exercício 4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantida e kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o valor a pagar de acordo com a tabela a seguir:
'''

# Dados fornecidos pelos usuários
while True:
    print('Vamos calcular o consumo de energia com base em algumas informações. Para isto, será necessário'
          'que você nos informe o seu consumo de energia em kWh e o tipo de instalação...')
    consumo = input('Digite o consumo em kWh:\n')
    tipo_instalação = input('Informe o tipo de instalação (R) para residencial, (C) para comercial e (I) para industrial:\n')

    if consumo.isdigit() and tipo_instalação.isupper():  # Verificador
        consumo = float(consumo)  # Convertendo o tipo de dados após a verificador
        message = 'O valor a ser pago pelo consumo será de'  # String para substituir nas mensagens

        if tipo_instalação == 'R' and consumo <= 500:
            consumo_calc = consumo * 0.40
            print(f'{message} R${consumo_calc:.2f}.')

        elif tipo_instalação == 'R' and consumo > 500:
            consumo_calc = consumo * 0.65
            print(f'{message} R${consumo_calc:.2f}.')

        elif tipo_instalação == 'C' and consumo <= 1000:
            consumo_cal = consumo * 0.55
            print(f'{message} R${consumo_cal:.2f}.')

        elif tipo_instalação == 'C' and consumo > 1000:
            consumo_cal = consumo * 0.60
            print(f'{message} R${consumo_cal:.2f}.')

        elif tipo_instalação == 'I' and consumo <= 5000:
            consumo_cal = consumo * 0.55
            print(f'{message} R${consumo_cal:.2f}.')

        else:
            consumo_cal = consumo * 0.60
            print(f'{message} R${consumo_cal:.2f}.')

    else:
        print('Digite os dados da forma que se pede.')  # Caso as entradas fornecidas não estejam de acordo