'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

titulo = str( 'ALISTAMENTO MILITAR' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

anoNasc = int( input( 'Em que ano você nasceu? ' ) )
anoAtual = date.today().year
idade = anoAtual - anoNasc

print( 'Quem nasceu em {} tem {} anos em {}'.format( anoNasc, idade, anoAtual ) )

if idade == 18:
    print( 'Você deve se alistar IMEDIATAMENTE!' )
elif idade < 18:
    falta = 18 - idade
    print( 'Ainda faltam {} anos para o seu alistamento, você deve se alistar em {}.'
    .format( falta, anoAtual + falta ) )
else:
    deve = idade - 18
    print( '''Você deveria ter se alistado há {} anos!
Seu alistamento foi em {}.'''.format( deve, anoAtual - deve ) )

print('''
EXERCITO BRASILEIRO, VOCÊ NÃO TEM ESCOLHA: É OBRIGATÓRIO!
''')

print( '==' * 31 )