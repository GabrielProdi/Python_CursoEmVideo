''' 
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
        Ex:
            Ana Maria de Souza
        primeiro: Ana
        último: Souza
'''

nome = str( input( 'Digite seu nome completo: ' ) ).strip().split()

print( 'Olá {}, seja bem vindo!\n'.format( ' '.join( nome ) ),
    'Seu primeiro nome é {}\n'.format( nome[0] ),
    'Seu último nome é {}'.format( nome[ len(nome) - 1 ] ) )
