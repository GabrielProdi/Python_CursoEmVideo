#Faca um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua area e a quantidade de tinta necessaria para pinta-la, 
# sabendo que cada litro de tinta pinta uma area de 2m²

medida1 = float( input( 'Digite a largura da parede em metros: ' ) )
medida2 = float( input( 'Digite a altura da parede em metros: ' ) )

litros = (medida1 * medida2) / 2

print( 'São necessários {}L de tinta para pintar a parede'.format( litros ) )
