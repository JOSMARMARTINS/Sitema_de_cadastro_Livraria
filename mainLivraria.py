def cadastrar_livro(id):
    '''
    Cadastra um novo livro no sistema
    :parâmetro id: Usado para identificar cada livro de maneira única no processo de catalogação
    '''
    global id_global  #acessando variável global
    id_global += 1
    nomeLivro = input('Por favor entre com o nome do livro: ')
    autorLivro = input('Por favro entre com o autor do livro: ')
    editoraLivro = input('Por favor entre com a editora do livro: ')
    catalogoLivro = {'id':id_global,'nome':nomeLivro,'autor':autorLivro,'editora':editoraLivro}  #dicionário para catologação dos livros
    lista_livro.append(catalogoLivro)  # insere o dicionário dentro e sempre ao final da lista_livro
    print('Livro Cadastrado com sucesso!')
    print('-' * qte_tracos)
    print()

def consultar_livro():
    '''
    :Consulta os livros: 1 lista todos os livros, 2 consulta os livros pelo id de catalogação, 3 consulta pelo nome do autor e 4 retorna ao menu principal.
    :return: ao usuário entrar com Sair dentro do submenu Consultar Livro o programa retorna ao Menu Pricipal

    '''
    # consultar todos os livros
    print('-' * qte_tracos)
    menu_consultar_livro = 'MENU CONSULTAR LIVRO'
    print(menu_consultar_livro.center(qte_tracos, '-'))
    opcaoDesejada = input('Escolha a opção desejada:\n1 - Consultar Todos os Livros\n2 - Consultar Livro por id\n3 - Consultar Livro(s) por autor\n4 - Retornar\n>> ')

    if opcaoDesejada == '1':
        print('-' * 20)
        if not lista_livro:
            print('Não há livros cadastrados!')  # Se não tiver livro cadastrado retorna uma mensagem para o usuário.
        else:
            for catalogoLivro in lista_livro:  # caso tenha exibe o catálogo de livros
                for chave, valor in catalogoLivro.items(): #vizualização de itens do dicionário
                    print(f'{chave}: {valor}') #print onde cada item é uma tupla que contém chave e valor
                print()
        print('-' * 20)
        print('-' * qte_tracos)
        print()

    # Consultar livro por id
    elif opcaoDesejada == '2':
        id = int(input('Digite o id do livro: '))
        print('-' * 20)
        idEncontrado = None
        for catalogoLivro in lista_livro:
            if catalogoLivro['id'] == id:
                idEncontrado = catalogoLivro
                break
        if idEncontrado:
            for chave, valor in idEncontrado.items():
                print(f'{chave}: {valor}')
        else:
            print('ID não localizada!')
        print()
        print('-' * 20)
        print(qte_tracos * '-')
        print()

    # Consulta por autor
    elif opcaoDesejada == '3':
        autorLivro = input('Digite o autor do(s) livro(s): ')
        print('-' * 20)
        livroEncontrado = False
        for catalogoLivro in lista_livro:
            if catalogoLivro['autor'] == autorLivro:
                livroEncontrado = True
                for chave, valor in catalogoLivro.items():
                    print(f'{chave}: {valor}')
                print()
        if not livroEncontrado:
            print('Autor não localizado!')
        print('-' * 20)
        print(qte_tracos * '-')
        print()

    #Retorna ao menu anterior
    elif opcaoDesejada == '4':
        return
    else:
        print("Opção inválida!")  #se não for uma opção válida, imprime a mensagem e retorna o loop
    consultar_livro()


def remover_livro():
    '''
    :return:  Remove o livro especificado pelo usuário com a entrada do id do livro
    '''
    idRemover = int(input('Digite o ID do livro a ser removido: '))
    for catalogoLivro in lista_livro:
        if catalogoLivro['id'] == idRemover:
            lista_livro.remove(catalogoLivro)
            print('Livro removido com sucesso!')
            break
    else:
        print('Id inválido!')
        remover_livro()




#PROGRAMA PRINCIPAL
print('Bem vindo a Livraria do Josmar Nascimento Martins')


lista_livro=[]  # Lista vazia
id_global = 0  #variável

  #Menu principal
while True:
    qte_tracos = 50  # usado para inserir todos os traços nos menus '-'
    print('-' * qte_tracos)
    menu_principal = 'MENU PRINCIPAL'
    print(menu_principal.center(qte_tracos,'-'))  #cabeçalho do MENU centralizado
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - sair')
    opcao_desejada = input('>> ')  #usuário entra com a opção desejada

    if opcao_desejada == '1':  #Cadastrar Livro
        print('-' * qte_tracos)
        menu_cadastrar_livro = 'MENU CADASTRAR LIVRO'
        print(menu_cadastrar_livro.center(qte_tracos, '-'))
        cadastrar_livro(id_global)
    elif opcao_desejada == '2':  #consultar livro
        consultar_livro()
        print('-' * 20)
        print('-' * qte_tracos)
        print()
    elif opcao_desejada == '3': #remover livro
        print('-' * qte_tracos)
        menu_remover_livro = 'MENU REMOVER LIVRO'
        print(menu_remover_livro.center(qte_tracos, '-'))
        remover_livro()
    elif opcao_desejada == '4':  # Encerrar o programa
        print("Pragrama finalizado!")
        break
    else:
        print('Opção inválida!')
        continue  #Volta ao loop caso a entrada seja != de 1, 2, 3 ou 4