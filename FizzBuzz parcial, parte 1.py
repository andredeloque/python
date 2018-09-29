numero = int(input("Digite um número para saber se é divisível por 3: "))
divisivel = numero % 3
if divisivel == 0:
    print ("Fizz")
else:
    print (numero)
