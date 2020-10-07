'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
    Ex: 
        Digite um número: 1834

        unidade: 4
        dezena: 3
        centena 8
        milhar: 1

'''

num = int( input( 'Digite um número inteiro não negativo de até quatro dígitos:  ' ) )

print( ' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}\n'
.format( num % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10 ) )
