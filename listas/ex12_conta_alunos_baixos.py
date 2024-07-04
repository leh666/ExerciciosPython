def conta_alunos_baixos(p_alturas, p_idades):    
    media=0
    for i in range (3):
        altura=p_alturas[i]
        media=media + altura
    media=media/3
    cont=0
    for i in range (3):
        idade=p_idades[i]
        altura=p_alturas[i]   
        if altura<media and idade>=13:
            cont=cont+1    
    return cont 