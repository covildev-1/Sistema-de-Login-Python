def verificar_cadastro(username, senha):
    indice = 0
    
    
    for usuario in users:
        nome = users[indice][0]
        password = users[indice][1]
        indice += 1
        
        
        if type(senha) == type(None):
            if username == nome:
                return False
            
            
    return True

def verificar_login(username, senha):
    indice = 0
    
    
    for usuario in users:
        nome = users[indice][0]
        password = users[indice][1]
        indice += 1
        
        
        if username == nome:
            if senha == password:
                return True
            else:
                return False
            
        
    return False
    

with open('Lista_de_Cadastros.txt', 'r+', encoding='Utf-8') as cadastros:
        users = []
        
        
        for linha in cadastros:
            linha = linha.split(',')
            x = [linha[0]] + [linha[1]]
            users.append(x)
            