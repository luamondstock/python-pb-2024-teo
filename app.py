
import os

def mostrar_opcoes():
    print('''

    ░█████╗░███╗░░██╗███████╗██╗░██████╗  ███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░░█████╗░░██████╗
    ██╔══██╗████╗░██║██╔════╝██║██╔════╝  ████╗░████║██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗██╔════╝
    ███████║██╔██╗██║█████╗░░██║╚█████╗░  ██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝██║░░██║╚█████╗░
    ██╔══██║██║╚████║██╔══╝░░██║░╚═══██╗  ██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗██║░░██║░╚═══██╗
    ██║░░██║██║░╚███║███████╗██║██████╔╝  ██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝╚█████╔╝██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░░╚════╝░╚═════╝░
    ''')


    print('1. Cadastrar cliente')
    print('2. Listar cliente')
    print('3. Ativar/Desativar cliente')
    print('4.Sair')

    opcao_escolhida = int(input ('Escolha uma opção:'))

    def cadastrar_cliente():
          print ('Você escolheu Cadastrar cliente')

    def listar_cliente():
          print ('Você escolheu Listar cliente') 

    def ativar_cliente():
          print ('Você escolheu Ativar/Desativar')

    def finaliza_programa ():
        os.system('cls')
        print ("finalizar_programa")

    if opcao_escolhida == 1:
        cadastrar_cliente()
    elif opcao_escolhida == 2:
        listar_cliente()
    elif opcao_escolhida == 3:
        ativar_cliente()
    else: 
        print ('Finalizar programa')

