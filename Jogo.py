from Seta_Jogadores import AjustaJogadores
from Cores import Seta_Cores_fonte
from time import sleep
from ValidaPalavra import ValidacaoPalavras
from ValidaTentativasDesafiado import ValidateTentativas
from LimpaTerminal import LimparTerminal


LimparTerminal.LimpaTerminal()
Seta_Cores_fonte.CorCyan('Bem Vindo ao Jogo da Forca, espero que se divirta!')
sleep(2)

Seta_Cores_fonte.CorCyan('Primeiramente este jogo tem apenas 2 jogadores aonde inicialmente você escolhe um deles para começar escolhendo uma palavra' +
' e o outro pode cometer até 6 erros ao tentar advinhar a palavra que o jogador desafiador escolheu!', 'S')
sleep(2)

vTerminouJogo = False
vPalavraDesafiador = ''

while not vTerminouJogo:
    # Utiliza o return do Get Jogadores. Primeiro valor se refere ao jogador Desafiador e o segundo ao Desafiado. 
    JogadorDesafiador, JogadorDesafiado = AjustaJogadores.GetJogadores()

    vPalavraDesafiador = ValidacaoPalavras.Validate_Palavra_Desafiador(JogadorDesafiado)
    vTerminouJogo = ValidateTentativas.Validate_Tentativas_Desafiado(vPalavraDesafiador)







