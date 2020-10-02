#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere US$ 1,00 = R$3,27

reais = float( input( 'Digite a quantidade de R$ que possui na carteira: R$' ) )

dolares = reais / 3.27 

print( 'Você pode comprar US${:.2f}'.format( dolares ) )