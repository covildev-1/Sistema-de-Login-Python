from constantes import caracteres


letras = caracteres[25:]


def verificar_username(nome):
    verificar = 1
    indice = 0
    erro = 0
    
    
    while verificar == 1:
        while indice < len(nome):
            if erro != 0:
                return False
        
        
            if nome[indice] in letras:
                indice += 1
            
            
            elif nome[indice] not in letras:
                erro += 1
                    
                    
        verificar -= 1
        
        
        return True