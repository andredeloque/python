import math
x1 = float(input("Digite o primeiro numero para X: "))
y1 = float(input("Digite o primeiro numero para Y: "))
x2 = float(input("Digite o segundo numero para X: "))
y2 = float(input("Digite o segundo numero para Y: "))
distancia = math.sqrt ((x1-x2)**2) + ((y1-y2)**2)
print (distancia)
if distancia >= 10:
    print ("longe")
if distancia <10:
    print ("perto")
