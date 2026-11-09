estoque = []


def cadastrar_produto():
    codigo = input("Digite o código do produto: ")

    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Erro: já existe um produto com esse código.")
            return

    nome = input("Digite o nome do produto: ")

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))

            if preco < 0:
                print("Erro: o preço não pode ser negativo.")
                continue

            break

        except ValueError:
            print("Erro: informe um preço válido.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))

            if quantidade < 0:
                print("Erro: a quantidade não pode ser negativa.")
                continue

            break

        except ValueError:
            print("Erro: informe uma quantidade válida.")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso!")


def calcular_total_estoque():
    total = 0

    for produto in estoque:
        total += produto["quantidade"]

    print(f"Quantidade total de produtos em estoque: {total}")


def menu():
    while True:
        print("\n--- CONTROLE DE ESTOQUE ---")
        print("1 - Cadastrar Produto")
        print("2 - Calcular Total de Produtos em Estoque")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            calcular_total_estoque()

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
