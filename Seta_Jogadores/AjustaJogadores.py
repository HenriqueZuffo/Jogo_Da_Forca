from Cores import Seta_Cores_fonte
from time import sleep
def GetJogadores():
    vJogador_Desafiador = 0
    vJogador_Desafiado = 0
    #  Percorre o while até o usuário informar o jogador correto.
    #  Após pegar o jogador desafiador ele ja seta o jogador desafiado. 
    while True:
        try:
            vJogador_Desafiador = int(input('Escolha entre os jogadores 1 e 2 para iniciar.\n'))
            
            if vJogador_Desafiador == 1:
                vJogador_Desafiado = 2
                break
            elif vJogador_Desafiador == 2:
                vJogador_Desafiado = 1
                break
            else:
                print('Apenas os jogadores 1 e 2 estão disponível!')
        except ValueError:
            print('Apenas numeros inteiros são aceitos.')
            
    # Printa para que o usuário tenha visualização de quem é o desafiador e o desafiante, e após isso da retorno. 
    Seta_Cores_fonte.CorCyan(f'O Jogador {vJogador_Desafiador} começa escolhendo a palavra e o jogador {vJogador_Desafiado} vai tentar acertar!')
    sleep(1.3) 
    # ATENÇÃO!
    # Não alterar o return, se não o jogo inteiro ficará com os papéis invertido. 
    return int(vJogador_Desafiador), int(vJogador_Desafiado)
    

