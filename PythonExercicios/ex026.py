''' 
    Faça um programa que leia uma frase pelo teclado e mostre:
        Quantas vezes aparece a letra "A"
        Em que posição ela aparece a primeira vez.
        Em que posição ela aparece a última vez
'''

frase = str( input( 'Digite uma frase: ' ) ).strip().upper()

print( 'Esta frase tem {} letras A\n'.format( frase.count( 'A') ) ,
        'O primeiro A aparece na posição {}\n'.format( frase.find( 'A' ) + 1 ), 
        'O último A aparece na posição {}\n'.format( frase.rfind( 'A' ) + 1 ) )
