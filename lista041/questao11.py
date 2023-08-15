'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num = int(input("Informe um número inteiro de 3 dígitos: "))
centenas = int(num / 100)
print(f"O algarismo das centenas é {centenas}.")