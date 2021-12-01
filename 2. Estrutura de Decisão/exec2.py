#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

#Entrada de dados e declaração de variáveis

num = int(input('Informe um número: '))

#Esturuta condicional

if(num >= 0):
    print('{} é um número positivo' .format(num))
if(num < 0):
    print('{} é um número negativo' .format(num))