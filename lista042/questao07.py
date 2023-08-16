'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

num = int(input("Me diga um número: "))
num2 = int(input("Me diga outro número: "))

if (num > num2):
    print(f"{num} é o maior número e {num2} é o menor número.")
if (num2 > num):
    print(f"{num2} é o maior número e {num} é o menor número.")
if (num == num2):
    print("Ambos os números são iguais.")