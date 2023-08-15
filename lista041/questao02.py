'''
Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se
a resposta está certa ou errada.
'''

capital = input("Qual a capital do Brasil? ")

if (capital == "Brasília"):
    print("Você acertou! A capital do Brasil é Brasília.")
else:
    print(f"Você errou! A capital do Brasil não é {capital}, é na verdade, Brasília.")
