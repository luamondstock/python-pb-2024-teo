import os

livros = [{'nome': 'Imperfeitos', 'genero': 'Young adult', 'ativo': True},
          {'nome': 'Divergente', 'genero': 'Distopia', 'ativo': False},
          {'nome': 'Pai Rico Pai Pobre', 'genero': 'Auto-ajuda', 'ativo': True}]
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
    print('1. Cadastrar livro')
    print('2. Listar livro')
    print('3. Ativar/Desativar leitura')
    print('4.Sair')

def escolhe_opcao():
        
    def exibir_subtitulo(texto):
        os.system('cls')
        print(texto)
        print ('')

    def retorna_menu():
        input(' Digite uma tecla para voltar ao menu principal')
        main()
            

    def cadastra_livro():
        exibir_subtitulo('Cadastrar livro')
        nome_livro = input('Digite o nome do livro que deseja cadastrar')
        livros.append(nome_livro)
        print(f'O livro {nome_livro} foi cadastrado com sucesso\n')
        retorna_menu()

    def listar_livro():
        exibir_subtitulo('Listar de livros cadastrados')

        for livro in livros:
            nome_livro = livro['nome']
            livro_genero = livro['genero']
            ativo = livro['ativo']
            print (f'- {nome_livro} | {livro_genero} | {ativo}')
        retorna_menu()
        
    
    def finaliza_programa():
        exibir_subtitulo("Finalizando o programa\n")
            

    def opcao_invalida():
        print('Opa, este carácter não é permitido\n')
        retorna_menu()
    
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))


        if opcao_escolhida == 1:
            cadastra_livro()
        elif opcao_escolhida == 2:
           listar_livro()
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

if __name__ == '__main__':
    main()
