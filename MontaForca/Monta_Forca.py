def MontarForca(Numero_Erros = 0, vLista_Letras_Encontradas = [], vPalavra_Desafiador = [], vLetrasChutes = []):
    vLetras_Encontradas = ''
    vPercorre_Letra_Palavra_Desafiador = ''
    vSeparaListaChutes = ', '
    vIndice_Letra = 0

    for vPercorre_Letra_Palavra_Desafiador in vPalavra_Desafiador:
        if vLista_Letras_Encontradas[vIndice_Letra] == 'S':
            vLetras_Encontradas = vLetras_Encontradas + ' ' + vPercorre_Letra_Palavra_Desafiador
        else:
            vLetras_Encontradas = vLetras_Encontradas + ' ' + '_'
        
        vIndice_Letra += 1
    
    if Numero_Erros == 0:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|      
|     
|     
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 1:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|        O      
|     
|     
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 2:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|       O     
|       |     
|     
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 3:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|        O     
|       /|     
|     
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 4:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|        O     
|       /|\\     
|     
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 5:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|        O     
|       /|\\     
|       /
|
|
|{vLetras_Encontradas}''')
    elif Numero_Erros == 6:
        print(f'''
.........|     Letras informadas: {vSeparaListaChutes.join(vLetrasChutes) if len(vLetrasChutes) >= 1 else ''}
|        O     
|       /|\\     
|       / \\
|
|
|{vLetras_Encontradas}''')
