'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Informe um valor númerico inteiro: "))

if  (num % 4 == 0 and num % 5 == 0):
    print("O seu número é {}.".format(num))
else:
    print("Seu número não é divisível por 4 e 5.")