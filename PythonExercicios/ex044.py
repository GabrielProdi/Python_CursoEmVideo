'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

titulo = str( ' LOJAS E DESCONTOS ' )
print( '=-' * 30 ) 
print( '{: ^60}'.format( titulo ) )
print( '=-' * 30 )

preco = float( input( 'Informe preço do produto: R$' ) )
opcao = int( input( '''Escolha a forma de pagamento:
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão
 Sua opção: ''' ) )


if opcao == 1 :
    total = preco * 0.9
    msg = str('com desconto de 10%')
elif opcao == 2 :
    total = preco * 0.95
    msg = str( 'com desconto de 5%')
elif opcao == 3:
    total = preco
    parcelas = total / 2
    msg = str( 'será parcelada em 2x de R${:.2f} SEM JUROS e'.format( parcelas ))
elif opcao == 4 :
    total = preco * 1.2
    vezes = int( input( 'Informe a quantidade de parcelas: ' ) )
    parcelas = total / vezes
    msg = str( 'será parcelada em {}x de R${:.2f} COM JUROS e'.format( vezes, parcelas ) )
else:
    print( 'OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE!' )
    exit()

print( 'Sua compra de R${:.2f}'.format( preco ), end=' ' )
print( msg, 'vai custar R${:.2f} no final.'.format( total ) )

print( '==' * 31 )