numero = int(input("Digite um número para saber se é divisível por 3 e 5: "))
por3 = numero % 3
por5 = numero % 5
if por3 == 0 and por5 == 0:
    print ("FizzBuzz")
else:
    print (numero)
