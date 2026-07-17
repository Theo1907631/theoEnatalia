from caixaAlta import caixaAlta
from dobro import dobro

def menu():
    while True:  
        print("\n================")
        print("Olá pessoal, tudo bem com vocês coleguinhas?\n" )
        print("P")
        print("1 - Caixa Alta")
        print("2 - Dobro do Número")
        print("3 - Sair")
        print("=====================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite uma palavra: ")
            resultado = caixaAlta(palavra)
            print(f"Resultado: {resultado}")

        elif opcao == "2":
            num = int(input("Digite um número: "))
            resultado = dobro(num, interruptor=1)
            print(f"O dobro de {num} é {resultado}")

        elif opcao == "3":
            print("Saindo... Até mais!")
            break  

        else:
            print("Opção inválida! Digite 1, 2 ou 3.")

menu()