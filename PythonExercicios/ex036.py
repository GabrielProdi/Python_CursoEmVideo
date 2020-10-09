'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

titulo = str( 'Análise de Empréstimo Bancário' )
centralizar = str( ' ' * int( ((60 - len(titulo)) / 2) ) )
print( '=-' * 31 ) 
print( centralizar, titulo, centralizar )
print( '=-' * 31 )

casa = float( input( 'Qual o valor da casa? ' ) )
salario = float( input( 'Qual o salário do comprador? ' ) )
anos = int( input( 'Quantos anos de financiamento? ' ) )

prestacao = casa / (12 * anos)

print( 'Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'
.format(casa, anos, prestacao) )

if prestacao <= (salario * 0.3):
    print( 'Empréstimo APROVADO!' )
else:
    print( 'Empréstimo NEGADO!' )

print( '==' * 31 )