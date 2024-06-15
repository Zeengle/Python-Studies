#--------------- LAB 6 -----------------------

#EX1-------------------
# import math
# a = int(input("Digite o primeiro lado do triangulo: "))
# b = int(input("Digite o segundo lado do triangulo: "))
# def hipotenusa (a,b):
#     return math.sqrt(a**2 + b**2)
# print(f"Hipotenusa: {hipotenusa(a,b):.2f}")
#--------------------

#EX2------------------
# planeta = str(input("Digite o o nome do planeta desejado: "))
# peso = float(input("Digite o peso da pessoa na Terra em kg: "))
# def pesoplaneta (planeta, peso):
#     if planeta == "Mércurio":
#         peso = peso*0.37
#         return peso
#     if planeta == "Vênus":
#         peso = peso*0.88
#         return peso
#     if planeta == "Marte":
#         peso = peso*0.38
#         return peso
#     if planeta == "Júpiter":
#         peso = peso*2.64
#         return peso
#     if planeta == "Saturno":
#         peso = peso*1.15
#         return peso
#     if planeta == "Urano":
#         peso = peso*1.17
#         return peso
#     if planeta == "Netuno":
#         peso = peso*1.18
#         return peso
# print(f"Peso em {planeta}: {pesoplaneta(planeta,peso):.2f}")
#---------------

#EX3-----------------
# def test_prime(num):
#     if num ==1:
#         return(False)
#     if num == 2:
#         return(True)
#     for i in range(2, num+1):
#         if num%i:
#             return(True)
#     else:
#         return (False)
#-------------------

#EX4--------------------
# def produtorio(*num):
#     num = list(num)
#     multi = 1
#     for i in num:
#         multi *= i
#     return multi
# print(produtorio(2,4,2,2))

#-----------------------

#EX5-----------------
# km = int(input("Digite a quantidade de quilometros: "))

# def tarifa(km):
#     tarifatot = 10+0.50*8*km
#     return (tarifatot)
# print(f"Tarifa {tarifa(km):.2f}")
#--------------------