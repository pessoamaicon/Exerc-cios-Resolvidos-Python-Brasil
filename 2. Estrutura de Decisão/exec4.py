#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

#Entrada de dados e declaração de variáveis

letra = str(input('Digite uma letra do alfabeto: '))
letra_min = letra.lower() #Força a string digitada para minúsculo.
vogais = list(['a', 'e', 'i', 'o', 'u'])

#Estrutura condicional

if (letra_min in vogais):
    print('A letra "{}" é uma vogal.' .format(letra_min))

else:
    print('A letra "{}" é uma consoante.' .format(letra_min))