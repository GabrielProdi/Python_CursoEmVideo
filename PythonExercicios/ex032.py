'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Para melhor entender

São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
Não são bissextos todos os demais anos.

'''
from datetime import date

ano = int( input( 'Me diga um ano qualquer: ' ) )

#Buscar o ano atual da máquina
if ano == 0:
    ano = date.today().year

# bissexto é divisível por 4 e não por 100 ou por 400
bissexto = ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0)

if bissexto:
    print( 'O ano {} é bissexto!'.format( ano ) )
else:
    print( 'O ano {} NÃO é bissexto!'.format( ano ) )