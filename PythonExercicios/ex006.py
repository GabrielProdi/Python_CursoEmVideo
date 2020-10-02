#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = int( input( 'Digite um numero: ' ) )
print( 'Seu dobro é {}, seu triplo é {} e a raiz quadrada é {:.2f}.'.format( (num*2), (num*3), (num**(1/2)) ))
