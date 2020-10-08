'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

distancia = float( input( 'Me diga a distância que percorrerá nesta viagem: ' ) )

print( 'O preço da sua passagem é R${:.2f}'.format(distancia * 0.5 if distancia <= 200 
        else distancia * 0.45) )

'''
if distancia <= 200:
    print( 'O preço da sua passagem é R${:.2f}'.format(distancia * 0.5) )
else:
    print( 'O preço da sua passagem é R${:.2f}'.format(distancia * 0.45) )
'''