#Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
preco = float( input( 'Digite o salário do funcionário: R$' ) )

print( 'O novo salário do funcionário será R${:.2f} !'.format( preco * 1.15 ) )
