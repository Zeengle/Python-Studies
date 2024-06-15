#-------------- LAB 5----------------------------

#EX1----------------
# linha = int(input("Digite a quantidade de linhas: "))
# for i in range(1, linha+1):
#     print(f"{i} {i**2} {i**3}")
#-----------------

#EX2----------
# n = int(input("Digite o número desejado: "))
# denominador = 1
# contador = 0
# somador = 1

# while denominador <n:
#     div = 1/denominador
#     somador += div
#     denominador += 1
# print(f"{somador+1/n:.3f}")
#---------------

#EX3--------------
# import math

# num = int(input("Digite o número desejado: "))
# for cont in range(2,num):
#     if (num%cont==0):
#         print("Número não primo")
#         break
#     else:
#         print("Número primo")
#         break
#--------------------

#EX4----------------
# num = int(input())
# num >5 and num <200

# contador = 0
# for i in range(num):
#     contador +=1
#     if contador %2==0:
#         print(f"{contador}^2 = {contador**2}")
#--------------------

#EX5----------------
# i = 1
# for j in range(60,-1,-5):
#     print(f"I={i} J={j}")
#     i +=3
#----------------------

#EX6-------------------
# while True:
#     num = int(input())
#     senha = 2024
#     if num !=senha:
#         print("Senha Invalida")
#     else:
#         print("Acesso Permitido")
#         break
#------------------------