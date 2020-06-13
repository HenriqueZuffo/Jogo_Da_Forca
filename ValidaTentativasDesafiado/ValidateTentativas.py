from ValidaPalavra import ValidacaoPalavras
from Cores import Seta_Cores_fonte
from MontaForca import Monta_Forca 
from LimpaTerminal import LimparTerminal

def Validate_Tentativas_Desafiado(PalavraDesafiador):
    PalavraDesafiador = PalavraDesafiador.upper()
    vLetrasTentativa = ''
    vEscolhaLP = ''
    vPercorreListaPDesafiador = ''
    vPercorreLPDesafiado = ''
    vSeparaListaChutes = ', '
    vTerminaJogo = ''

    vPontuacaoDesafiado = 0
    vPontuacaoDesafiador = 0
    vNumeroTentativas = 0
    vPercorrePalavra = 0
    vIndice_Letra = 0
    
    vListaPalavraDesafiador = []
    vListaLetraEncontrada = []
    vListaChutes = []
    vLista_Desagrupa_Palavra_desafiado = []
    
    vEncontrouLetra = False
    vProx_Jogada = False
    

    while vPercorrePalavra < len(PalavraDesafiador):                
        vListaPalavraDesafiador.append(PalavraDesafiador[vPercorrePalavra])
        if PalavraDesafiador[vPercorrePalavra] == '-':
            vListaLetraEncontrada.append('S') 
        else:   
            vListaLetraEncontrada.append('N')
        vPercorrePalavra += 1

    # Percorre ao total 6 vezes que é o número de tentativas que usuário tem. 
    while True:
        # Limpa a variável, apenas por precaução.
        vLetrasTentativa = ''
        vProx_Jogada = False
        vNumeroTentativas += 1

        LimparTerminal.LimpaTerminal()
        # Verifica agora se encontrou letra pois abaixo é setado como False novamente.
        if vNumeroTentativas > 1:
            if vEncontrouLetra:
                Seta_Cores_fonte.CorVerde('Acertou! Parabéns!')
            else:
                Seta_Cores_fonte.CorVermelha('Que pena, você errou :(')
                vPontuacaoDesafiador += 1
        
        if Verifica_Achou_Todas_Letras(vListaLetraEncontrada):
            vPontuacaoDesafiado = 6
        
        if vPontuacaoDesafiado == 6 or vPontuacaoDesafiador == 6:
            if vPontuacaoDesafiado == 6:
                Seta_Cores_fonte.CorMagenta('Parabéns jogador desafiado você venceu o jogo!')
            else:
                Seta_Cores_fonte.CorMagenta('Parabéns jogador desafiador você venceu o jogo!')
                print(f'A palavra escolhida pelo Desafiador foi: {PalavraDesafiador}' )
            
            while True:
                try:
                    vTerminaJogo = input('Você deseja jogar novamente?')
                    vTerminaJogo = vTerminaJogo.upper()

                    if vTerminaJogo == 'N':
                        return True
                    elif vTerminaJogo == 'S':
                        return False
                    else:
                        Seta_Cores_fonte.CorCyan('Apenas S ou N são aceitos como resposta!', 'S')
                except:
                    print('Erro:' + Exception)

        Monta_Forca.MontarForca(vPontuacaoDesafiador, vListaLetraEncontrada, vListaPalavraDesafiador, vListaChutes)
        
        #  Passa como false toda vez que o usuário for informar uma letra ou palavra.
        vEncontrouLetra = False 
        while not (vProx_Jogada):
            # Caso for 1 significa que é a primeira vez passando dentro deste for
            if vNumeroTentativas == 1:
                Seta_Cores_fonte.CorCyan('Atenção, na primeira rodada apenas letras podem ser escolhidas')
                vEscolhaLP = 'L'
            else:
                Seta_Cores_fonte.CorCyan('Caso deseje chutar uma Palavra, só poderá realizar uma tentativa de acerto, caso erre perde o jogo caso acerte ganha o jogo.')
                vEscolhaLP = str(input('Deseja informar uma letra ou uma palavra? Digite L para informar uma letra ou P para palavra\n'))
                
            vEscolhaLP = vEscolhaLP.upper()
            vEscolhaLP = vEscolhaLP.strip()            
            
            if vEscolhaLP == '':
                Seta_Cores_fonte.CorCyan('Informe ao menos uma letra!','S')
            elif not(vEscolhaLP) in 'LP':
                Seta_Cores_fonte.CorCyan('Apenas as Letras L e P são permitidas!','S')
            else:
                if ((vEscolhaLP == 'L') or (vNumeroTentativas == 1)):
                    vLetrasTentativa = input(Seta_Cores_fonte.ApenasNegrito("Digite uma letra que você acha que está na palavra escolhida pelo desafiador!\n"))
                    vLetrasTentativa = vLetrasTentativa.upper()    
                    vLetrasTentativa = vLetrasTentativa.strip() 

                    if vLetrasTentativa == '':
                        Seta_Cores_fonte.CorCyan('Informe ao menos uma letra!','S')
                        vProx_Jogada = False                     
                    if len(vLetrasTentativa) > 1:
                        Seta_Cores_fonte.CorCyan('Digite apenas uma letra!','S')
                        vProx_Jogada = False
                    elif ValidacaoPalavras.Validate_Palavra(vLetrasTentativa, 'S', 'S'):                        
                        vPercorreListaPDesafiador = ''
                        
                        if vLetrasTentativa in vListaChutes:
                            Seta_Cores_fonte.CorVermelha('A letra já foi utilizada anteriormente!')
                            vProx_Jogada = False
                            break 
                            
                        vListaChutes.append(vLetrasTentativa)

                        vIndice_Letra = 0
                        for vPercorreListaPDesafiador in vListaPalavraDesafiador:
                            if vLetrasTentativa == vPercorreListaPDesafiador:
                                vListaLetraEncontrada[vIndice_Letra] = 'S'
                                vProx_Jogada = True
                                vEncontrouLetra = True 
                            else:
                                vProx_Jogada = True

                            vIndice_Letra +=1
                        
                elif ((vEscolhaLP == 'P') and (vNumeroTentativas > 0)):
                    vLetrasTentativa = input(Seta_Cores_fonte.ApenasNegrito("Digite uma palavra que você acha que é a palavra escolhida pelo desafiador!\n"))
                    vLetrasTentativa = vLetrasTentativa.upper()    
                    vLetrasTentativa = vLetrasTentativa.strip()

                    
                    if vLetrasTentativa == '':
                        Seta_Cores_fonte.CorCyan('Informe ao menos duas letras!','S') 
                        vProx_Jogada = False                     
                    if len(vLetrasTentativa) == 1:
                        Seta_Cores_fonte.CorCyan('Informe mais que uma letra','S')
                        vProx_Jogada = False
                    elif ValidacaoPalavras.Validate_Palavra(vLetrasTentativa, 'S', 'S'):                        
                        # Passa o valor máximo para assim sair do for.
                        # False
                        vPercorreListaPDesafiador = ''
                        vPercorreLPDesafiado = ''
                        vIndice_Letra = 0

                        vLetrasTentativa = ValidacaoPalavras.Ajusta_Palavra_Composta(vLetrasTentativa)
                        for vPercorreLPDesafiado in vLetrasTentativa:
                            vLista_Desagrupa_Palavra_desafiado.append(vPercorreLPDesafiado)
                        
                        
                        for vPercorreListaPDesafiador in vListaPalavraDesafiador:
                            if vListaPalavraDesafiador[vIndice_Letra] != vLista_Desagrupa_Palavra_desafiado[vIndice_Letra]:
                                vPontuacaoDesafiador = 5
                                vProx_Jogada = True
                                vEncontrouLetra = False
                                break
                            else:
                                vPontuacaoDesafiado = 5
                                vEncontrouLetra = True
                                vProx_Jogada = True
                                vListaLetraEncontrada[vIndice_Letra] = 'S'
                            vIndice_Letra += 1


def Verifica_Achou_Todas_Letras(Letras_Encontradas):
    vIndice_Letra = 0
    vVeririficaLetras = ''

    for vVeririficaLetras in Letras_Encontradas:
        if vVeririficaLetras == 'S':
            vIndice_Letra +=1
        else:
            vIndice_Letra -=1
    
    if vIndice_Letra == len(Letras_Encontradas):
        return True
    else:
        return False