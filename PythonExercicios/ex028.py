'''         Jogo da adivinhação v1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu. 
'''
from time import sleep
from random import randint

print( '='*60, '\nVou pensar em um número entre 0 e 5. Tente adivinhar...' )
num = int( input( 'Qual número eu pensei? ' ) )

print( 'PROCESSANDO...' )
sleep(1)    #comando para pausar o processamento (importar biblioteca 'time')

computador = randint( 0, 5 )

if num == computador :
    print( 'PARABÉNS!! Você adivinhou certo!' )
else:
    print( 'GANHEI! Eu pensei no número {} e não no {}.'.format( computador, num ) )