'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num1 = int( input( 'Primeiro valor: ' ) )
num2 = int( input( 'Segundo valor: ' ) )
num3 = int( input( 'Terceiro valor: ' ) )

'''
# em lógica direta
if num1 > num2: 
    if num1 > num3:
        print( 'O maior valor digitado foi {}'.format( num1 ) )
        if num2 > num3:
            print( 'O menor valor digitado foi {}'.format( num3 ) )
        else:
            print( 'O menor valor digitado foi {}'.format( num2 ) )
    else:
        print( 'O maior valor digitado foi {}'.format( num3 ) )
        print( 'O menor valor digitado foi {}'.format( num2 ) )
elif num2 > num3:
    print( 'O maior valor digitado foi {}'.format( num2 ) )
    if num1 > num3:
        print( 'O menor valor digitado foi {}'.format( num3 ) )
    else:
        print( 'O menor valor digitado foi {}'.format( num1 ) )
else:
    print( 'O maior valor digitado foi {}'.format( num3 ) )
    print( 'O menor valor digitado foi {}'.format( num1 ) )

'''

# Verificando o menor
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando o maior
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# Mostrando a resposta para o usuário
print( 'O menor valor digitado foi {}'.format( menor ) )
print( 'O maior valor digitado foi {}'.format( maior ) )