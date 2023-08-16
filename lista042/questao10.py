'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

nome = input("Qual o seu nome? ")
n1 = float(input("Qual a nota da sua primeira prova? "))
n2 = float(input("Qual a nota da sua segunda prova? "))
media = (n1 + n2)/2

if (media < 3):
    print(f"Sua média é {media}. Você está reprovado.")
elif (media > 3 and media < 6.9):
    print(f"Sua média é {media}. Você está de prova final.")
else:
    print(f"Sua média é {media}. Você está aprovado!")
