#Faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

num = int( input( 'Digite um número inteiro: ' ) )

print( '{}\nA tabuada do {} é:'.format( ('-'*20), num ) )
for i in range(1, 11, 1):
    print ( '{} x {:2} = {:2}'.format( num, i, (num*i) ) )

print( '-'*20 )