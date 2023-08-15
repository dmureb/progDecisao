'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Informe um número inteiro: "))

'''
if (num >=1 and num <=10):
    print("Seu número está entre 1 e 10!")
else:
    print("Seu número não está entre 1 e 10.")
'''

#var = (se for falso, se for verdadeiro)[teste condicional]
resposta = (f"{num} não está na faixa de 1 a 10", f"{num} está na faixa de 1 a 10")[num >=1 and num <=10]
print(resposta)