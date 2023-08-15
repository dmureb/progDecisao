'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

a = int(input("Informe um valor: "))
b = int(input("Informe outro valor: "))
c = int(input("Informe um último valor: "))

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