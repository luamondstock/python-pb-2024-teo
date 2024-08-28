import os
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
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))

        def cadastra_cliente():
            os.system('cls'),
            print('Cadastro de novos clintes\n')
            nome_cliente = input('Digite o nome do cliente que deseja cadastrar')
            clientes.append(nome_cliente)
            print(f'O cliente {'nome_cliente'} foi cadastrado com sucesso\n')
            input(' Digite uma tecla para voltar ao menu principal ')
            main()
            
        
        def finaliza_programa():
            os.system("cls")
            print('Finalizando o programa')

        def opcao_invalida():
            print('Opa, este caracter não é permitido\n')
            input('Aperte qualquer tecla para voltar')
            main()

        if opcao_escolhida == 1:
            print('Você escolheu Cadastrar cliente')
        elif opcao_escolhida == 2:
            print('Você esacolheu Listar livro')
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

