s = 0
n = 0
carrinho = {}
prudutos = {1:'Banana', 2:'Maçã', 3:'Abacaxi', 4:'Tomate', 5:'Alho'}

while True:
    cod_prod = input('Selecione um dos produtos abaixo:\n (1) Banana = R$0,50kg\n (2) Maçã = R$1,00kg\n (3) Abacaxi = R$4,00kg\n (4) Tomate = R$7,00kg\n (5) Alho = R$8,00kg\n Ou pressione s para sair para finaliarmos a sua compra.\n')


    if cod_prod == 's' or cod_prod == 'S':
        print(f'A sua compra ficou no valor de R${s:5.2f}.\n Até a próxima!')
        break

    elif not cod_prod.isnumeric():
        print('Código Inválido. Selecione o código do produto informado na tela incial e tente novamente mais tarde.')
        break

    quant_prod = input('Digite a quantidade comprada:\n')

    if not quant_prod.isnumeric():
        print('Quantidade inválida. Execute o programa novamente com a quantidade em kg correta!')
        break

    if cod_prod.isnumeric() and quant_prod.isnumeric():
        quant_prod = int(quant_prod)
        cod_prod = int(cod_prod)

        if cod_prod == 1:
            calc = quant_prod * 0.5
        elif cod_prod == 2:
            calc = quant_prod * 1.
        elif cod_prod == 3:
            calc = quant_prod * 4
        elif cod_prod == 4:
            calc = quant_prod * 7
        elif cod_prod == 5:
            calc = quant_prod * 8

    s += calc  # Acomulador
    carrinho[prudutos[cod_prod]] = calc

    print(f'Total até o momento: = R${s:5.2f}.')

    new_buy = input('Deseja realizar outra compra ou sair? (S) para sair ou (C) para realizar outra compra...\n')

    if new_buy == 'S' or new_buy == 's':
        print('Seus itens do carrinho são:')
        for key, item in carrinho.items():
            print(f'{key} R${item:5.2f}')
        print(f'Total: R${s:5.2f}.')
        break

    elif new_buy == 'C' or new_buy == 'c':
        print('É sempre um prazer atender você...')

    else:
        print(' Entrada inválida, digite S para sair ou (C) para realizar outra compra.')


