#Escreva um programa que leia em metros e exiba convertido em centimetros e milimetros 

medida = float( input( 'Digite a medida em metros: ' ) )

cm = medida * 10 ** (2)
mm = medida * 10 ** (3)

print( 'Esta medida é de {}cm ou {}mm '.format( cm, mm ) )
