'''
 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

num1 = int( input( 'Me diga o primeiro número: ' ) )
num2 = int( input( 'Me diga o segundo número: ' ) )

if num1 == num2:
    print( 'NÃO existe valor maior, os dois são iguais' )
elif num1 < num2:
    print( 'O SEGUNDO valor é maior' )
else:
    print( 'O PRIMEIRO valor é maior' )
    