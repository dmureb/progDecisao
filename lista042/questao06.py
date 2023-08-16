'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

ano = int(input("Qual seu ano de nascimento? "))
ano2 = int(input("Em que ano estamos? "))
idade = ano2 - ano

if (ano > ano2):
    print("Dados inseridos estão incorretos.")
else:
    print(f"Você tem {idade} anos.")