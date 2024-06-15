#-------------LAB 4---------------------------------

#EX1------------
# import math
# while True:
#     p0x = input("valor de X para P0: ")
#     if p0x == "sair":
#         break
#     p0y = int(input("valor de Y para P0: "))
#     p1x = int(input("valor de X para P1: "))
#     p1y = int(input("valor de Y para P1: "))

#     print(f"Distancia de {math.sqrt((int(p0x)-p1x)**2 + (p0y-p1y)**2)}")
#------------------

#EX2-----------------
# n = int(input("Digite o número desejado: "))
# denominador = 1
# contador = 0
# somador = 1

# while denominador <n:
#     div = 1/denominador
#     somador += div
#     denominador += 1
# print(f"{somador+1/n:.3f}")
#----------------------

#EX3-----------------
# n = int(input("Digite n: "))
# m = int(input("Digite m: "))
# if n < m:
#     d = n
# else:
#     d = m
# while (m%d !=0 or n%d !=0):
#     d -=1
# print(d)
#--------------------

#EX4---------------------
# x = int(input("Digite o numero desejado: "))
# palpite = x/2
# erro = palpite**2-x
# while erro >10**-12:
#     palpite = (palpite+(x/palpite))/2
#     erro = palpite**2 - x
# print(f"{palpite:.3f}")
#------------------------

#EX5-----------------
# s = 0
# n = 1
# while n!=0:
#     n = int(input())
#     s += n
# print(f"Resultado: {s}")
#------------------------


