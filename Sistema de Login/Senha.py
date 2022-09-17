from constantes import caracteres

def verificar_senha(senha):
    verificar = 1
    indice = 0
    erro = 0
    
    
    while verificar == 1:
        while indice < len(senha):
            if erro != 0:
                return False
            
            
            if senha[indice] in caracteres:
                indice += 1
            
            
            elif senha[indice] not in caracteres:
                erro += 1
                
                
        verificar -= 1
    
        
        return True