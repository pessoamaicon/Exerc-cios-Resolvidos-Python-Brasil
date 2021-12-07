#Faça um Programa que leia três números e mostre-os em ordem decrescente.

#Entrada de dados e declaração de variáveis.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

print('[{}, {}, {}]' .format(num1, num2, num3))

#Estrutura condicional

if(num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux
    
if(num2 > num1):
    aux = num2
    num2 = num1
    num1 = aux
    
if(num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux
    
print('[{}, {}, {}]' .format(num1, num2, num3))