#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

#Entrada de dados e declaração de variáveis

turno = str(input('Informe o turno que você estuda, digite: M-Matutino, V-Vespertino, N-Noturno: '))
letra_upper = turno.upper() #Força a string digitada para maiúsculo

#Estrutura condicional

if (letra_upper == 'M'):
    print('Bom Dia!')

elif (letra_upper == 'V'):
    print('Boa Tarde!')
    
elif (letra_upper == 'N'):
    print('Boa Noite!')
    
elif (letra_upper != 'M' or letra_upper != 'V' or letra_upper != 'N'):
    print('Valor Inválido!')


