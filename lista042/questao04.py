'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Me diga um número de 1 a 7: "))

if (num == 1):
    print("Segunda-feira")
if (num == 2):
    print("Terça-feira")
if (num == 3):
    print("Quarta-feira")
if (num == 4):
    print("Quinta-feira")
if (num == 5):
    print("Sexta-feira")
if (num == 6):
    print("Sábado")
if (num == 7):
    print("Domingo")
if (num > 7):
    print("Seu número não é válido.")