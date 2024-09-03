import os

livros = [{'nome': 'Imperfeitos', 'genero': 'Young adult', 'ativo': True},
          {'nome': 'Divergente', 'genero': 'Distopia', 'ativo': False},
          {'nome': 'Pai Rico Pai Pobre', 'genero': 'Auto-ajuda', 'ativo': True}
          
          ]
def mostra_titulo():
    print('''


█▄▄ █ █▄▄ █░░ █ █▀█ ▀█▀ █▀▀ █▀▀ ▄▀█   █▀▄▀█ █▀█ █▀█ █▄░█
█▄█ █ █▄█ █▄▄ █ █▄█ ░█░ ██▄ █▄▄ █▀█   █░▀░█ █▄█ █▄█ █░▀█
        ''')

def mostra_escolhas():
    print('1. Cadastrar livro')
    print('2. Listar livro')
    print('3. Ativar/Desativar leitura')
    print('4.Sair\n')

def escolhe_opcao():
        
    def exibir_subtitulo(texto):
        os.system('cls')
        linha  = '*' * len (texto)
        print(linha)
        print(texto)
        print(linha) 
        print ('')

    def retorna_menu():
        input(' Digite uma tecla para voltar ao menu principal')
        main()
            

    def cadastra_livro():
        exibir_subtitulo('Cadastrar livro')
              
        nome_livro = input('Digite o nome do livro que deseja cadastrar')
        livro_genero = input(f'Digite o genero de {nome_livro} que irá cadastrar')
        dados_do_livro = {'nome': nome_livro, 'genero': livro_genero, 'ativo': True}
        livros.append(dados_do_livro)
        print(f'O livro {nome_livro} foi cadastrado com sucesso\n')

        retorna_menu()

    def listar_livro():
        exibir_subtitulo('Listar livros cadastrados')

          print(f'{Nome do livro'.ljust(22)} | {'livro'.ljust(20)} | Status ')
          for livro in livros:
            nome_livro = livro['nome']
            livro_genero = livro['genero']
            ativo = 'Ativado' if livro['ativo'] else 'Desativado'
            print (f' - {nome_livro.ljust(20)]} | {livro_genero.ljust(20)} | {ativo}')
              
        retorna_menu()

          

    def ativar_leitura():
        exibir_subtitulo('Ativar leitura') 
        nome_livro = input ('Digite o nome do livro para ativar:') 
        livro_encontrado = False

        for livro in livros:
            if nome_livro == livro['livro']:
                livro_encontrado = True
                livro ['ativo'] = not livro ['ativo']
                mensagem = f'O cadastro de {nome_livro} foi ativado com sucesso'if livro['ativo'] else f'O cadastro {nome_livro} foi desativado'
                print(mensagem)
                      
            if not livro_encontrado:
                  print('Não encontrado') 
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
           ativar_leitura()
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
