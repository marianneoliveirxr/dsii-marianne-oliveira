def cadastrar_pessoas():
    cadastrados = []  # Lista para armazenar os cadastros

    while True:
        # recebendo as informações do usuário para cadastro
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = input("Digite a idade: ")

        # armazenando o cadastro 
        pessoa = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade}

        # verificando duplicação pelo nome
        # 'f' serve para formatação,assim não precisa concatenar 
        if any(v['nome'] == nome for v in cadastrados):
            print(f"O cadastro para o nome '{nome}' já existe.")
        else:
            cadastrados.append(pessoa)  # adicionado no final da lista pelo .append
            print(f"Cadastro de {nome} {sobrenome} feito com sucesso!")

        # pergunta se deseja cadastrar outras pessoas 
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar == 'n':
            break
        # .strip(): remove qualquer espaço em branco no início ou no final da resposta do usuário
        # .lower(): converte a resposta para minúsculas

    # mostra o total de pessoas cadastradas
    print(f"\nTotal de cadastros realizados: {len(cadastrados)}")

    # mostra as pessoas cadastradas
    print("\nPessoas cadastradas:")
    for p in cadastrados:
        print(f"{p['nome']} {p['sobrenome']} - Idade: {p['idade']}")

# chama a função e fim
cadastrar_pessoas()
