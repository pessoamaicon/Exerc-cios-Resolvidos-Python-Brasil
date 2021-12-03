#Faça um Programa que leia três números e mostre o maior deles. 

#Entrada de dados e declaração de variáveis

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

#Estrutura Condicional

if(num1 > num2 and num1 > num3):
    print('{} é o maior número' .format(num1))

if(num2 > num1 and num2 > num3):
    print('{} é o maior número' .format(num2))
    
if(num3 > num1 and num3 > num2):
    print('{} é o maior número' .format(num3))


