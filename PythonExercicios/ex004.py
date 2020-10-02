# Leia algo e mostre na tela os tipos primitivos e todas as informacoes sobre ele

a = input( 'Digite algo: ' )
print( 'O tipo primitivo deste valor é {}'.format( type( a ) ))
print( 'Só tem espaços? {}'.format( a.isspace() ) )
print( 'É numérico? {}'.format( a.isnumeric() ) )
print( 'É alfabético? {}'.format( a.isalpha() ) )
print( 'É alfanumérico? {}'.format( a.isalnum() ) )
print( 'Está em maiúsculas? {}'.format( a.isupper() ) )
print( 'Está em minúsculas? {}'.format( a.islower() ) )
print( 'Está em capitalizada? {}'.format( a.istitle() ) )
