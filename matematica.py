a = float(input("insira o valor de a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))
delta = b**2-4*a*c
if delta < 0:
    print ("Delta menor que 0")
else:
    print ("delta = ", delta)
    raizDelta=delta**0.5
    print ("raiz de delta = ", raizDelta)
    x1 = (-b+raizDelta) / (2*a)
    print ("x1 = ", x1)
    x2 = (-b-raizDelta) / (2*a)
    print ("x2 = ", x2)
