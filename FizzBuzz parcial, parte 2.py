numero = int(input("Digite um número para saber se é divisível por 5: "))
divisivel = numero % 5
if divisivel == 0:
    print ("Buzz")
else:
    print (numero)
