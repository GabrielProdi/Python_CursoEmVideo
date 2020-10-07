''' 
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
        Ex:
            Ana Maria de Souza
        primeiro: Ana
        último: Souza
'''

nome = str( input( 'Digite seu nome completo: ' ) ).strip()
n = nome.split()

print( 'Olá {}, seja bem vindo!\n'.format(nome),
    'Seu primeiro nome é {}\n'.format( n[0] ),
    'Seu último nome é {}'.format( n[ len(n) - 1 ] ) )
