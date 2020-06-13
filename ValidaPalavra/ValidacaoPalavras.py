from Cores import Seta_Cores_fonte
from LimpaTerminal import LimparTerminal
from time import sleep
def Validate_Palavra_Desafiador(vJogadorDesafiado):
    vPalavra = ''
    vMsg = ''
    # Percorre o while até o usuário informar uma palavra.
    while True:
        sleep(1)
        LimparTerminal.LimpaTerminal()
        # Utilizado variável pois não estava conseguindo printar de forma que eu queria. ## Gambiarra
        Seta_Cores_fonte.CorCyan('Atenção ao digitar uma palavra composta, irá ser subtituído o ESPAÇO por HÍFEN', 'S')
        sleep(1.3)
        vPalavra = input(f'Escolha a palavra que deseja que o jogador {vJogadorDesafiado} advinhe.\n')
        if len(vPalavra) <= 1:
            # Utiliza o fonte para deixar a palavra 'UMA' em negrito, para assim dar destaque na hora do usuário ler.
            print(f'A palavra deve conter mais que {Seta_Cores_fonte.ApenasNegrito("UMA")} letra')
        else:
            vPalavra = Ajusta_Palavra_Composta(vPalavra)
            if Validate_Palavra(vPalavra, 'S'):
                break
    return vPalavra


def Validate_Palavra(Palavra = str, Mostra_Msg = 'N', Valida_Hifen = 'N'):
    condicao = '()*&¨%$#@!¹²³£¢¬:><.,^~][´`_=+/?|\ }{ùúàáãõóòìíçÙÚÀÁÃÕÓÒÌÍÇ123456789' if Valida_Hifen == 'N' else '()*&¨%$#@!¹²³£¢¬:><.,^~][´`_=+/?|\ }{ùúàáãõóòìíçÙÚÀÁÃÕÓÒÌÍÇ123456789-'

    if Palavra in condicao:
        if Mostra_Msg == 'S':
            if Valida_Hifen == 'N':
                Seta_Cores_fonte.CorCyan('Por favor informe apenas letras!(Único caracter além das letras que é permitido é o HÍFEN', 'S')
            else:
                Seta_Cores_fonte.CorCyan('Por favor informe apenas letras!', 'S')
        return False
    else:
        return True

def Ajusta_Palavra_Composta(Palavra):
    vPalavra = ''
    vPalavra = Palavra    
    return vPalavra.replace(' ', '-')