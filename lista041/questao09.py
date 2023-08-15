'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número inteiro: "))

if (num > 0):
    print("Seu número é positivo!")
elif (num == 0):
    print("Seu número é nulo!")
else:
    print("Seu número é negativo!")
