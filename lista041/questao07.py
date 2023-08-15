'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Informe um número inteiro positivo ou negativo: "))
neg = num * (-1)

if (num >= 0):
    print(f"O módulo desse número é {num}.")
else:
    if  (num < 0):
        print(f"O módulo desse número é {neg}.")