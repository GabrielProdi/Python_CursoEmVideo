''' 
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

speed = float( input( 'Qual a velocidade atual do carro? ' ) )

if speed > 80:
    print( 'O limite de velocidade da via é 80Km/h!\n'
    'Você será multado em R${:.2f}'.format( (speed - 80) * 7 ) )

print( 'Tenha um bom dia! Dirija com segurança!' )