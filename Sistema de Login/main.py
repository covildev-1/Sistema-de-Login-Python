from Cadastro import cadastro
from Login import login


def main():
    resposta = input('Fazer novo cadastro ou fazer login (Digite "cadastro" ou "login")? ')


    while resposta.lower() != 'cadastro' and resposta.lower() != 'login':
        print('ERROR: Resposta inválida!')
        
        
        resposta = input('Fazer novo cadastro ou fazer login (Digite "cadastro" ou "login")? ')


    if resposta.lower() == 'cadastro':
        cadastro()
        
        print('Cadastro feito com Sucesso!')
        print('Seja bem-vindo!')
    else:
        login()
        
        print('Seja bem-Vindo de volta!')


main()