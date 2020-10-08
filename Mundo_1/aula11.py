'''     CORES NO TERMINAL       '''
# \033[ style ; text ; bg m
''' 
style:                      text ( 30 ~ 39 ) - backgroud ( 40 ~ 49 )
    0 - none                        X0 - white
    1 - bold                        X1 - red
    4 - underline                   X2 - green
    7 - negative                    X3 - yelow           
                                    X4 - blue
                                    X5 - purple
                                    X6 - cian
                                    X7 - gray
'''
nome = 'Gabriel'
print( '\033[1;32;41mOlá Mundo!\033[m' )
print( 'Muito prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m' ) )