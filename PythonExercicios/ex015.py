#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro cusata R$60 por dia e 
# R$0,15 por Km rodado

dias = int ( input( 'Quantos dias o carro foi alugado?' ) )
kms = float( input( 'Quantos Km o carro alugado rodou?' ) )

pagar = (dias * 60) + (kms * 0.15)

print( 'O total a ser pago é R${:.2f}'.format( pagar ) )
