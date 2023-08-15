'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

a = int(input("Informe um valor: "))
b = int(input("Informe outro valor: "))
c = int(input("Informe um último valor: "))

'''
if (a < b < c):
    print(f"Em ordem crescente: {a, b, c}.")
if (a < c < b):
    print(f"Em ordem crescente: {a, c, b}.")
if (b < a < c):
    print(f"Em ordem crescente: {b, a, c}.")
if (b < c < a):
    print(f"Em ordem crescente: {b, c, a}.")
if (c < a < b):
    print(f"Em ordem crescente: {c, a, b}.")
if (c < b < a):
    print(f"Em ordem crescente: {c, b, a}.")
'''

# 1- a tem que ser menor que b
if  (a > b):
    aux = a
    a = b
    b = aux

#garantido até aqui que entre a e b, o menor está em a

# 2- a tem que ser menor que c
if  (a > c):
    aux = a
    a = c
    c = aux

# garantido até aqui que a é o menor dos 3
# agora é necessário garantir que b seja menor que c

if  (b > c):
    aux = b
    b = c
    c = aux
# garantido até aqui que entre b e c, o b é menor, ou seja, o c é maior de todos

print(f"Ordem crescente: {a}, {b} e {c}")






















