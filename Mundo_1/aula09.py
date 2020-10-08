'''Manipulando texto'''

frase = '   Curso em Video Python   '

print( frase )
print( len( frase ) )
print( frase.count(' ') )
print( len( frase.strip() ) )
print( frase.replace( 'Python', 'Android' ) )
print( frase.lower().strip() )
print( frase.upper().strip() )

dividido = frase.split()
print( dividido )