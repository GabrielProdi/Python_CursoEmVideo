'''     CONDIÇÕES ANINHADAS    '''

nome = str( input( 'Qual é o seu nome? ' ) )

if nome == 'Gabriel':
    print( 'Que nome bonito!' )
elif nome == 'Pedro' or nome == 'Maria':
    print( 'Seu nome é bem popular no Brasil!' )
else:
    print( 'Seu nome é bem normal...' )

print( 'Tenha um bom dia {}!'.format( nome ) )
