from dobro import dobro 

palavras = []

def menu():
    while True: 
        print("\n======= MENU =======")
        print("1 - Caixa Alta")
        print("2 - Dobro do Número")
        print("3 - Sair")
        print("=====================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite uma palavra: ")
            resultado = dobro(palavra)
            print(f"Resultado: {resultado}")

        elif opcao == "2":
            num = int(input("Digite um número: "))
            resultado = dobro(num)
            print(f"O dobro de {num} é {resultado}")

        elif opcao == "3":
            print("Saindo... Até mais!")
            break 

        else:
            print("Opção inválida! Digite 1, 2 ou 3.")


menu()



