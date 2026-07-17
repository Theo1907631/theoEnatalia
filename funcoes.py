from caixaAlta import caixaAlta
from dobro import dobro


print("Olá! Tudo bem, coleguinha? A seguir um menu para acessar as funções:")

while True:
    print('''
    +-----MENU DE FUNÇÕES-----+
        1-Código da Natalia
        2-Código do Theo
        0-Sair
    +-------------------------+
    ''')

    while True:
        try:
            menu = int(input("Digite uma opção númerica: "))

            if menu < 0 or menu > 2:
                print("\nPor favor, digite uma das opções númericas\n")
            else:
                break
        except:
            print("\nO valor digitado deve ser um número inteiro!\n")

    if menu == 1:
        while True:
            caixaAlta(interruptor=1)

            print("Deseja sair do código da Natalia?")

            while True:
                try:
                    menuNatalia = int(input("Digite 1 para 'Sim' e 0 para 'Não':"))

                    if menuNatalia < 0 or menuNatalia > 1:
                        print("\nPor favor, digite uma das opções númericas\n")
                    else:
                        break
                except:
                    print("\nO valor digitado deve ser um número inteiro!\n")

            if menuNatalia == 1:
                break
            else:
                continue
    elif menu == 2:
        while True:
            dobro(interuptor = 1)

            print("Deseja sair do código do Theo?")

            while True:
                try:
                    menuTheo = int(input("Digite 1 para 'Sim' e 0 para 'Não':"))

                    if menuTheo < 0 or menuTheo > 1:
                        print("\nPor favor, digite uma das opções númericas\n")
                    else:
                        break
                except:
                    print("\nO valor digitado deve ser um número inteiro!\n")

            if menuTheo == 1:
                break
            else:
                continue
    elif menu == 0:
        break
    else:
        print("\n[ERROR!] Algo deu errado no sistema.\n")