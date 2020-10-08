''' Condições parte 1 '''


nome = str( input( 'Qual é o seu nome? ' ) )

if nome == 'Gabriel':
    print( 'Que nome lindo você tem!' )
else:
    print( 'Seu nome é tão normal...' )

print( 'Bom dia {}!'.format( nome ) )

print('='*60)

n1 = float( input( 'Digite a primeira nota: ' ) )
n2 = float( input( 'Digite a segunda nota: ' ) )

m = (n1 + n2) / 2
print( 'A sua média foi {:.1f}'.format( m ) )
'''
if m >= 6.0:
    print( 'Sua média foi boa! Parabéns!' )
else:
    print( 'Estude mais um pouco!' )
'''
print( 'Sua média foi boa! Parabéns!' if m >= 6.0 else 'Estude mais um pouco!' )