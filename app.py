import os

livros = ('livro': 'Imperfeitos', 'genero': 'Young adult', 'ativo': True),
        ('livro': 'Divergente', 'genero': 'Distopia', 'ativo': False),
        ('livro': 'Pai Rico Pai Pobre', 'genero': 'Auto-ajuda', 'ativo': True),

def mostra_titulo():
    print('''

        ░█████╗░███╗░░██╗███████╗██╗░██████╗  ███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░░█████╗░░██████╗
        ██╔══██╗████╗░██║██╔════╝██║██╔════╝  ████╗░████║██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗██╔════╝
        ███████║██╔██╗██║█████╗░░██║╚█████╗░  ██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝██║░░██║╚█████╗░
        ██╔══██║██║╚████║██╔══╝░░██║░╚═══██╗  ██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗██║░░██║░╚═══██╗
        ██║░░██║██║░╚███║███████╗██║██████╔╝  ██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝╚█████╔╝██████╔╝
        ╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░░╚════╝░╚═════╝░
        ''')

def mostra_escolhas():
    print('1. Cadastrar cliente')
    print('2. Listar livro')
    print('3. Ativar/Desativar leitura')
    print('4.Sair')

def escolhe_opcao():
        
        def exibir_subtitulo(texto)
            os.system('cls')
            print(texto)
            print ('')

        def retorna_menu():
            input(' Digite uma tecla para voltar ao menu principal ')
            main()
            

    
        def cadastra_cliente():
            os.system('cls'),
            print('Cadastro de novos clintes\n')
            nome_cliente = input('Digite o nome do cliente que deseja cadastrar')
            clientes.append(nome_cliente)
            print(f'O cliente {'nome_cliente'} foi cadastrado com sucesso\n')
            retorna_menu()

        def listar_livro():
             exibir_subtitulo('Lista de alunos cadastrados')
            for livro in clientes
                print (f'--(aluno)')

            input (' Digite uma tecla para voltar ao menu principal')
            main()

        
    
        def finaliza_programa():
            os.system("cls")
            print('Finalizando o programa\n')

        def opcao_invalida():
            print('Opa, este caracter não é permitido\n')
            input('Aperte qualquer tecla para voltar')
            main()
    
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))


        if opcao_escolhida == 1:
            print('Você escolheu Cadastrar cliente')
        elif opcao_escolhida == 2:
            print('Você escolheu Listar livro')
        elif opcao_escolhida == 3:
            print('Você escolheu Ativar leitura')
        elif opcao_escolhida == 4:
            finaliza_programa()
        else :
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()
opcao_escolhida = int(input('Escolha uma opção:'))

if __name__ == '__main__':
    main()

