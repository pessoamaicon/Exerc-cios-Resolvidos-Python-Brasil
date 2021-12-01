#Faça um Programa que peça dois números e imprima o maior deles. 

#Entrada de dados e declaração de variáveis

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))

#Esturuta condicional

if(num1 > num2):
    print('{} maior que {}' .format(num1, num2))
else:
    print('{} maior que {}' .format(num2, num1))