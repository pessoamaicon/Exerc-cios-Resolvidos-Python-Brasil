#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#Entrada de dados e declaração de variáveis

preco1 = float(input('Informe o preço do primeiro produto: '))
preco2 = float(input('Informe o preço do segundo produto: '))
preco3 = float(input('Informe o preço do terceiro produto: '))

#Estrutura Condicional

if(preco1 < preco2 and preco1 < preco3):
    print('Você deve comprar o primeiro produto de valor: R${}' .format(preco1))
    
if(preco2 < preco1 and preco2 < preco3):
    print('Você deve comprar o segundo produto de valor: R${}' .format(preco2))
    
if(preco3 < preco1 and preco3 < preco2):
    print('Você deve comprar o terceiro produto de valor: R${}' .format(preco3))


