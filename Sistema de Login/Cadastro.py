from Senha import verificar_senha
from Usuario import verificar_username
from Gerador import gerar_senha
from Verificar import verificar_cadastro


def cadastro():
    def validacao_user(user):
        while not verificar_username(user):    
            print('Nome de usuário inválido!')
            print('O nome de usuário deve conter apenas letras maiúsculas e minúsculas.')
            
            
            user = input('Usuário: ')
            
            
        while not verificar_cadastro(user, None):
            print('Nome de usuário já existente!')
            
            
            user = input('Usuário: ')
            
            
            return validacao_user(user)
        
        
        return user
    
    
    def validacao_senha(senha):
        while len(senha) < 8:
            print('Senha inválida!')
            print('A senha deve conter no mínimo 8 caracteres.')
            
            
            senha = input('Senha: ')
            
        
        while not verificar_senha(senha):
            print('Senha inválida!')
            print('A senha deve conter letras, números e caracteres como "()*:-+@!?&%$~^_"')
            
            senha = input('Senha: ')
            
            
            return validacao_senha()
        
        
        return(senha)
        
    
    senha = ''
    temp_user = input('Usuário: ')
    user = validacao_user(temp_user)


    resposta = input('Deseja colocar uma senha sugerida (Y/N)? ')


    if resposta.upper() == 'N':
        temp_senha = input('Senha: ')
        senha = validacao_senha(temp_senha)


    while resposta.upper() == 'Y':
        sugestão0 = gerar_senha()
        sugestão1 = gerar_senha()
        sugestão2 = gerar_senha()
        sugestão3 = gerar_senha()
        sugestão4 = gerar_senha()
        
        
        print('Opção 1: ' + sugestão0)
        print('Opção 2: ' + sugestão1)
        print('Opção 3: ' + sugestão2)
        print('Opção 4: ' + sugestão3)
        print('Opção 5: ' + sugestão4)
        
        
        resposta = input('Deseja continuar com alguma das senhas sugeridas (Y/N)? ')
        
        
        if resposta.upper() == 'N':
            resposta = input('Gerar nova senha (Y/N)? ')
            
            
            if resposta.upper() == 'N':
                break
            
            
        else:
            resposta = int(input('Digite o número da opção: '))
            
            
            if resposta == 1:
                senha = sugestão0
                break
            elif resposta == 2:
                senha = sugestão1
                break
            elif resposta == 3:
                senha = sugestão2
                break
            elif resposta == 4:
                senha = sugestão3
                break
            elif resposta == 5:
                senha = sugestão4
                break
    
    
    with open('Lista_de_Cadastros.txt', 'a') as cadastros:
        cadastros.writelines(user + ',' + senha + ',\n')
    
    
    return user, senha
