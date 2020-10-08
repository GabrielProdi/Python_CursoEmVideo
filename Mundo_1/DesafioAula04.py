#Desafio 01:
#           Recebe o nome e escreve em frase formatada 

print ( '======== DESAFIO 01 ========' )
nome = input ( 'Qual é o seu nome? ' )
print ( 'Olá ' + nome + '! Prazer em te conhecer!')

#Desafio 02:
#           Recebe o dia, mes e ano de nascimento e escreve em frase formatada

print ( '======== DESAFIO 02 ========' )
print ( 'Quando você nasceu?' )
dia = input ( 'Dia = ' )
mes = input ( 'Mes = ' )
ano = input ( 'Ano = ' )
print ( 'Você nasceu no dia ' , dia , ' de ' , mes , ' de ' , ano)

#Desafio 03:
#           Recebe dois numeros e escreve a soma deles

print ( '======== DESAFIO 03 ========' )
num1 = int( input ( 'Digite um número: ' ) )
num2 = int( input ( 'Digite mais um número: ') )
soma = num1 + num2
print ( 'A soma dos números é {}'.format( soma ) )
