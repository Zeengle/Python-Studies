#-------------- LAB 8 ---------------------------------------
#EX1--------------
# palavra = str(input())
# vogais = ["a", "e", "i", "o", "u"]
# for i in palavra:
#     if i in vogais:
#         print(f"{i.upper()}", end='')
#     else:
#         print(f"{i}",end='')
#--------------------

#EX2------------------
# palavra = str(input())
# revers = palavra.replace(' ','')
# reverso = revers[::-1]
# if revers == reverso:
#     print("É palindromo")
# else:
#     print("Não é palindromo")
#---------------------

#EX3------------------------
# from arquivo import palavras
# maior = ''
# for i in palavras:
#     if len(i) > len(maior):
#         maior = i
# print(maior)
#-----------------------------

#EX4---------------------------
# from arquivo import palavras
# arrumas = []
# for i in palavras:
#     arruma = i.upper().replace("!","")
#     arrumas.append(arruma)
# maior = 0
# for i in arrumas:
#     if arrumas.count(i) > maior:
#         maior = arrumas.count(i)
# print(f"contador: {maior}")
#------------------------------

#EX5--------------------------
# palabra = str(input())
# if palabra[0] in ["a", "e", "i", "o", "u"]:
#     palabra += "way"
# else:
#     final =''
#     for i in palabra:
#         if i not in ["a", "e", "i", "o", "u"]:
#             final = final +i
#             nova = palabra.replace(final, "")
#         else:
#             print(nova+final+"ay")
#             break
#-----------------------------