'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = int(input("Informe um número: "))

if (num > 20):
    metade = num/2
    print("A metade deste número é {}".format(metade))
else:
    print("O número é {}".format(num))
print("FIM DO PROGRAMA")