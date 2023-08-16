'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla = input("Me diga uma sigla de um estado brasileiro: ")

if (sigla == "RJ"):
    print("Rio de Janeiro é um estado da região Sudeste.")
if (sigla == "SP"):
    print("São Paulo é um estado da região Sudeste.")
if (sigla == "MG"):
    print("Minas Gerais é um estado da região Sudeste.")
if (sigla == "ES"):
    print("Espírito Santo é um estado da região Sudeste.")
else:
    print("Esse estado não se localiza na região Sudeste.")