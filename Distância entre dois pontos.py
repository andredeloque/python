import math
x1 = float(input("Digite o primeiro numero para X1: "))
y1 = float(input("Digite o primeiro numero para Y1: "))
x2 = float(input("Digite o segundo numero para X2: "))
y2 = float(input("Digite o segundo numero para Y2: "))
distancia = math.sqrt (((x2-x1)**2) + ((y2-y1)**2))
print (distancia)
if distancia >= 10:
    print ("longe")
if distancia <10:
    print ("perto")
