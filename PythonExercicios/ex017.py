''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''

from math import hypot

catOpo = float( input( 'Comprimento do cateto oposto: ' ) )
catAdj = float( input( 'Comprimento do cateto adjacente: ' ) )

#hip = ( catOpo**2 + catAdj**2  ) ** (1 / 2)
hip = hypot( catOpo, catAdj )

print( 'O comprimento da hipotenusa é {:.2f}'.format(hip) )
