'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
titulo = str( 'IMC' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

peso = float( input( 'Informe o seu peso (kg): ' ) )
altura = float( input( 'Informe a sua altura (m): ' ) )

imc = peso / (altura**2)

print( 'O seu IMC é {:.2f}, portanto você está na faixa de '
.format( imc ), end='' )

if imc > 40 :
    print( 'Obesidade Mórbida. CUIDADO!!' )
elif imc > 30 :
    print( 'Obesidade! ' )
elif imc > 25 :
    print( 'Sobrepeso.' )
elif imc > 18.5 :
    print( 'Peso Ideal.' )
else:
    print( 'Abaixo do Peso.' )

print( '==' * 31 )