'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
titulo = str( 'Analisador de Triângulos' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

a = float( input( 'Primeiro segmento: ' ) )
b = float( input( 'Segundo segmento: ' ) )
c = float( input( 'Terceiro segmento: ' ) )

if a < b + c and b < a + c and c < a + b:
    print( 'Os segmentos acima PODEM formar triângulo' )
else:
    print( 'Os segmentos acima NÃO PODEM formar triângulo' )