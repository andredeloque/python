a = float(input("insira o valor de a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))
delta = b**2-4*a*c
raizDelta=delta**0.5
x1 = (-b+raizDelta) / (2*a)
x2 = (-b-raizDelta) / (2*a)
if delta < 0:
    print ("esta equação não possui raízes reais")
if delta == 0:
    print ("a raiz desta equação é ", x1)
if delta > 0:
    if x1 < x2:
        print ("as raízes da equação são X", x1,"e Y", x2)
    else:
        print ("as raízes da equação são Y", x2,"e X", x1)
