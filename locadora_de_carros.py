import os

#cliente = { '0': 'Mostrar portifólio |', '1': 'Alugar um carro |', '2': 'Devolver um carro |'}
carros = [
    ('Chevrolet Tracker', 120),
    ('Chevrolet Onix', 90),
    ('Hyundai HB20', 85),
    ('Chevrolet Tucson', 120),
    ('Fiat Uno', 60),
    ('Chevrolet Mobi', 70),
    ('Chevrolet Pulse', 130)
]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):

        print('[{}] {} - R$ {} /dia'.format(i, car[0],car[1]))

while True:
    os.system('clear')

    print('==================')
    print('Bem vindo a locadora de Veículos')
    print('==================')
    print('')
    print('O que deseja fazer?')
    print('')
    print('0 - Mostrar portifólio |1 - Alugar um carro | 2 - Devolver um carro |')
    op = int(input())

    os.system('clear')
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print('==================')
        print('Escolha o código do carro')
        cod_car = int(input())
        print('Por quantos dias você pretende alugar este carro?')
        dias = int(input())
        os.system('clear')

        print(' Você escolheu o {} por {} dias.'.format(carros[cod_car][0], dias))
        print('')
        print('O aluguel totalizaria R${}. Deseja alugar? '.format(dias * carros[cod_car][1]))
        print('')
        print('0 - SIM | 1 - NÃO')
        conf = int(input())
        if conf == 0:
            print('Parabéns você alugou o {} por {}.'.format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print('Não tem carros para devolução')
        else:
            print('Segue a lista de carros alugados. Deseja devolver?')
            print('')
            print('Escolha o código do carro que deseja devolver:')
            cod = int(input())
            if conf == 0:
                print(' Obrigado por devolver o carro {}'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))
        

        print('')
        print('============')
        print('0 para CONTINUAR | 1 para SAIR')
        if float(input()) == 1:
            break



