#Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto
preco = float( input( 'Digite o preço do produto: R$' ) )

print( 'Você pagará apenas R${:.2f} neste produto!'.format( preco * 0.95 ) )
