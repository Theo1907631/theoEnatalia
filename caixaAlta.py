def caixaAlta ():

    while True:
        item = input("Digite uma palavra: ")

        if item == "":
            print("\nPor favor, não deixe o campo vázio.\n")
        else:
            break

    print("\n+------------+\n")
    print(f"A palavra {item} em caixa alta é escrita como {item.upper()}")


caixaAlta()

