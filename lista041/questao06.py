'''

 Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Informe um valor numérico inteiro: "))
num2 = int(input("Informe outro valor numérico inteiro: "))
dif1 = num1 - num2
dif2 = num2 - num1

if (num1 > num2):
    print(f"A diferença entre {num1} e {num2} é igual a {dif1}.")
else:
    if (num2 > num1):
        print(f"A diferença entre {num2} e {num1} é igual a {dif2}.")