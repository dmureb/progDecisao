'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Me diga a sua idade: "))
resposta = ("Você é menor de idade", "Você é maior de idade")[idade >= 18]