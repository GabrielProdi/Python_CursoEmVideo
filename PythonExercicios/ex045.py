'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

titulo = str( 'JOKENPÔ' )
print( '=-' * 30 ) 
print( '{: ^60}'.format(titulo) )
print( '=-' * 30 )

itens = ('PEDRA', 'PAPEL', 'TESOURA')

print( 'Vamos jogar Jokenpô!!' )
player = int( input( '''Escolha sua opção: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Sua jogada: ''' ) )

print( 'JO' )
sleep(1)
print( 'KEN' )
sleep(1)
print( 'PO!!!' )

computador = randint( 0, 2 )

print( '=-' * 20, '=' )
print( 'Jogador jogou {}'.format( itens[player - 1] ) )
print( 'Computador jogou {}'.format( itens[computador] ) )
print( '=-' * 20, '=' )

if player - 1 == computador :               # Ambos jogaram a mesma coisa
    print( 'EMPATE!' )
else:
    if player == 1:                         # Jogador jogou PEDRA
        if computador == 1:                 # Computador jogou PAPEL
            print( 'Computador VENCEU!' )
        else:                               # Computador jogou TESOURA
            print( 'Jogador VENCEU!' )

    elif player == 2 :                      # Jogador jogou PAPEL
        if computador == 2:                 # Computador jogou TESOURA
            print( 'Computador VENCEU!' )
        else:                               # Computador jogou PEDRA
            print( 'Jogador VENCEU!' )

    elif player == 3 :                      # Jogador jogou TESOURA
        if computador == 0:                 # Computador jogou PEDRA
            print( 'Computador VENCEU!' )
        else:                               # Computador jogou PAPEL
            print( 'Jogador VENCEU!' )


print( '==' * 31 )