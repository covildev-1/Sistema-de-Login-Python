import random
from constantes import caracteres


def gerar_senha():
    senha_forte = []
    
    
    while len(senha_forte) < 12:
        numeros = caracteres[:10]
        especiais = caracteres[10:25]
        letras_min = caracteres[25:51]
        letras_mai = caracteres[51:]
        
        
        tupla = (random.choice(numeros),
                random.choice(especiais),
                random.choice(letras_min),
                random.choice(letras_mai))
        
        
        senha_forte.append(random.choice(tupla))
        
        
    senha = (senha_forte[0] +
          senha_forte[1] +
          senha_forte[2] +
          senha_forte[3] +
          senha_forte[4] +
          senha_forte[5] +
          senha_forte[6] +
          senha_forte[7] +
          senha_forte[8] +
          senha_forte[9] +
          senha_forte[10] +
          senha_forte[11])
    
    return senha