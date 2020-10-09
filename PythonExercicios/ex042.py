'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

titulo = str( 'Analisador de Triângulos v2.0' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

a = float( input( 'Primeiro segmento: ' ) )
b = float( input( 'Segundo segmento: ' ) )
c = float( input( 'Terceiro segmento: ' ) )

if a < b + c and b < a + c and c < a + b:
    print( 'Os segmentos acima PODEM formar um triângulo ',end='' )
    if a == b == c:
        print( 'EQUILÁTERO.' )
    elif a != b != c != a:
        print( 'ESCALENO.' )
    else:
        print( 'ISÓSCELES.' )
else:
    print( 'Os segmentos acima NÃO PODEM formar triângulo' )

print( '==' * 31 )