'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

from datetime import date

titulo = str( 'CATEGORIA NATAÇÃO' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

anoNasc = int( input( 'Em qual ano o atleta nasceu? ' ) )
anoAtual = date.today().year
idade = anoAtual - anoNasc

print( 'Quem nasceu em {} tem {} anos em {} e está na categoria '
.format( anoNasc, idade, anoAtual ), end='' )

if idade > 25 :
    print( 'MASTER.' )
elif idade > 19 :
    print( 'SÊNIOR.' )
elif idade > 14 :
    print( 'JÚNIOR.' )
elif idade > 9 :
    print( 'INFANTIL.' )
else:
    print( 'MIRIM.' )

print( '==' * 31 )