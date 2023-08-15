'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

num1 = float(input("Me informe sua primeira nota: "))
num2 = float(input("Me informe sua segunda nota: "))
num3 = float(input("Me informe sua terceira nota: "))
num4 = float(input("Me informe sua quarta nota: "))

media = (num1 + num2 + num3 + num4)/4

if (media >= 5):
    print(f"Você foi aprovado! Sua média final foi {media}")
else:
    print(f"Você infelizmente foi reprovado. Sua média final foi {media}")
