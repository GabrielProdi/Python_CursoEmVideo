'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math as m

theta = float( input( 'Digite o ângulo: ' ) )

cos = m.cos( m.radians( theta ) )
sen = m.sin(  m.radians( theta )  )
tg = m.tan(  m.radians( theta )  )

print( 'Para o ângulo de {}º, o seno vale {:.2f}, o cosseno vale {:.2f} e a tangente vale {:.2f}'.format( theta, sen, cos, tg ) )
