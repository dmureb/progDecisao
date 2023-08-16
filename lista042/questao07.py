'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

num = int(input("Me diga um número: "))
num2 = int(input("Me diga outro número: "))

if (num > num2):
    print(f"{num} é maior que {num2}")
if (num2 > num):
    print(f"{num2} é maior que {num}")
if (num == num2):
    print(f"{num} é igual a {num2}")