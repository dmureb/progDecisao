'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000
'''

num = int(input("Me diga um número: "))
resposta = "Seu número está acima de 1000" if num > 1000 else "Seu número está abaixo de 1000"
print(resposta)