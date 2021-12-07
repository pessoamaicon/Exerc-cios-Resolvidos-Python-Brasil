#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

#Entrada de dados e declaração de variáveis

nota = float(input('Informe uma nota de 0 a 10: '))

#Estrutura de repetição

while(nota > 10):
    nota = float(input('Informe uma nota de 0 a 10: '))
    continue
print('A nota informada é {}'. format(nota))
       