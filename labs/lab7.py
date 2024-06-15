#---------- LAB 7 ----------------------------------------

#EX1---------------------
# carros = []
# kms = []

# for i in range(5):
#     carros.append(input())
# i = 0
# for x in range(5):
#     kms.append(int(input()))
#     if kms[x] > kms[i]:
#         i = x
# print(carros[i])

# for i in kms:
#     print(round(1000/i))
#---------------------------

#EX2----------------
# import math

# lista = []
# qtd = int(input("Qual o tamanho da lista: "))
# print("Digite os valores:")
# for i in range(qtd):
#     lista.append(int(input()))

# media = 0
# for num in lista:
#     media +=num
# media = media/qtd

# dp = 0
# for num in lista:
#     dp +=(num-media)**2
# dp = dp/qtd
# dp = math.sqrt(dp)

# print(f"Média = {media:.2f} e Desvio = {dp:.2f}")
#----------------

#EX3-------------------
# neg = []
# pos = []

# while True:
#     num = int(input())
#     if num == 0:
#         break
#     neg.append(str(num)) if num < 0 else pos.append(str(num))

# print(", ".join(neg))
# print(", ".join(pos))
#---------------------------

#EX4---------------
# par = []
# impar = []

# for n in range(20):
#     n = int(input())
#     if n%2==0:
#         par.append(n)
#     else:
#         impar.append(n)
#--------------------

#EX5------------------
# print("Digite o vetor 1:")
# vt1 = []
# for i in range(3):
#     vt1.append(int(input()))
# print("Digite o vetor 2:")
# vt2 = []
# for i in range(3):
#     vt2.append(int(input()))

# soma = 0
# for i in range(3):
#     soma +=vt1[i]*vt2[i]
# print(soma)

#-----------------------

#EX6-----------------
# def quadrado(lista):
#     for i in range(len(lista)):
#         lista[i] = lista[i]**2
#     return lista
# print(quadrado([1,2,3,4,5,6,7]))
#-------------------