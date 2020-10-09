'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

titulo = str( 'MÉDIA FINAL' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

nota1 = float( input( 'Primeira nota: ' ) )
nota2 = float( input( 'Segunda nota: ' ) )

media = (nota1 + nota2) / 2
print( 'Sua média foi {:.1f}, portanto você está '.format( media ), end='' )

if media < 5.0 :
    print( 'REPROVADO!' )
elif media >=7.0 :
    print( 'APROVADO!' )
else:
    print( 'de RECUPERAÇÃO!' )

print( '==' * 31 )