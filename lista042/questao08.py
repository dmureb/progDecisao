'''
 azer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

num1 = int(input("Me informe um número: "))
num2 = int(input("Me informe outro  número: "))
num3 = int(input("Me informe um último número: "))

maior = num1

if (maior < num2):
    maior = num2
if (maior < num3):
    maior = num3
print(f"O maior número inserido é {maior}.")