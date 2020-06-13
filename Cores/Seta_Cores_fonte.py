def CorVermelha(Msg = str, Negrito = 'N', Retorna = 'N'):
    vMsg = ''
    if Negrito == 'S':
        vMsg = ('\033[1;91m' + Msg + '\033[0;0m')
    else:
        vMsg = ('\033[0;91m' + Msg + '\033[0;0m')

    if Retorna == 'N':
        print(vMsg)
    else:
        return vMsg  
    
def CorVerde(Msg = str, Negrito = 'N', Retorna = 'N'):
    vMsg = ''
    if Negrito == 'S':
       vMsg = ('\033[1;92m' + Msg + '\033[0;0m')
    else:
        vMsg = ('\033[0;92m' + Msg + '\033[0;0m')

    if Retorna == 'N':
        print(vMsg)
    else:
        return vMsg

def CorCyan(Msg = str, Negrito = 'N', Retorna = 'N'):
    vMsg = ''
    if Negrito == 'S':
        vMsg = ('\033[1;36m' + Msg + '\033[0;0m')
    else:
        vMsg =('\033[0;36m' + Msg + '\033[0;0m')

    if Retorna == 'N':
        print(vMsg)
    else:
        return vMsg 
    
def CorAmarela(Msg = str, Negrito = 'N', Retorna = 'N'):
    vMsg = ''
    if Negrito == 'S':
        vMsg =('\033[1;33m' + Msg + '\033[0;0m')
    else:
        vMsg =('\033[0;33m' + Msg + '\033[0;0m')

    if Retorna == 'N':
        print(vMsg)
    else:
        return vMsg   

def CorMagenta(Msg = str, Negrito = 'N', Retorna = 'N'):
    vMsg = ''
    if Negrito == 'S':
        vMsg = ('\033[1;95m' + Msg + '\033[0;0m')
    else:
        vMsg = ('\033[0;95m' + Msg + '\033[0;0m')

    if Retorna == 'N':
        print(vMsg)
    else:
        return vMsg

def ApenasNegrito(Msg = str):
    vMsg = ''
    vMsg = ('\033[;1m' + Msg + '\033[0;0m' )
    return vMsg


# Cores retiradas dos Sites: https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
# https://gist.github.com/natorsc/8de21b65036d5965346ad4a779e72e28
# https://pythonhoje.wordpress.com/2018/01/28/python-3-cores/