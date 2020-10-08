#Operadores Aritmeticos

n1 = int( input('Digite um número: ' ) )
n2 = int( input('Digite outro número: ' ) )

soma = n1 + n2
prod = n1 * n2
div = n1 / n2
divint = n1 // n2
exp = n1 ** n2
resto = n1 % n2

# {: } os dois pontos formatam o valor da mascara conforme as diretrizes
#quebra de linha é \n  
# end= escrever o conteudo no final do print
print( 'A soma é {}, \no produto é {} \ne a divisão é {:.2}. '.format( soma, prod, div ), end='' )
print( 'A divisão inteira é {}, \na potenciação é {} \ne o resto da divisão é {}'.format( divint, exp, resto ) )