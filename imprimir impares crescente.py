numero = int(input("Digite o valor de n: " ))
iniciador = 1
while iniciador <= numero:
    if (numero % 2 == 0):
        if iniciador >= 0:
            print (iniciador)
            iniciador = iniciador + 2
    else:
        if iniciador >= 0:
            print (iniciador)
            iniciador = iniciador + 2
