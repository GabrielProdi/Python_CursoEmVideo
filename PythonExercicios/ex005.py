#Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

num = int( input( 'Digite um numero: ' ) )
print( 'Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format( num, (num-1), (num+1) ) )
