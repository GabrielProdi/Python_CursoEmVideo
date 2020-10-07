''' 
Crie um programa que leia o nome completo de uma pessoa e mostre: 
        O nome com todas as letras maiúsculas
        O nome com todas as letras minúsculas
        Quantas letras ao todo (sem considerar espaços)
        Quantas letras tem o primeiro nome
'''

nome = str( input( 'Digite seu nome completo: ' ) ).strip()

print( 'Analisando seu nome... \n   Seu nome em maiúsculas: {}\n    Seu nome em minúsculas: {}\n    Seu nome tem ao todo {} letras\n    Seu primeiro nome tem {} letras'
.format( nome.upper(), nome.lower(), len(nome)-nome.count( ' ' ), nome.find( ' ' ) ) )
#print( len( nome.split()[0] ) )
