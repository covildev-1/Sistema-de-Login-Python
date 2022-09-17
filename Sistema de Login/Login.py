from Verificar import verificar_login


def login():
    username = input('Usuário: ')
    senha = input('Senha: ')
    
    
    while username == senha:
        print('Nome de usuário e senha devem ser diferentes!')
        
        username = input('Usuário: ')
        senha = input('Senha: ')
    
    
    while not verificar_login(username, senha):
        print('Nome de usuário ou senha incorretos!')
        
        
        username = input('Usuário: ')
        senha = input('Senha: ')
    
    
    return username, senha
