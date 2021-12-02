#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

#Declaração de variáveis e Entrada de dados

str1 = str(input('Informe o sexo F-Feminino ou M-Masculino: '))
str_upper = str1.upper() #Força a string digitada para maiúsculo.

#Estrutura Condicional

if (str_upper == 'F'):
    print('Sexo {}-Feminino' .format(str_upper))
    
elif (str_upper == 'M'):
    print('Sexo {}-Masculino' .format(str_upper))
    
else:
    print('Sexo Inválido')