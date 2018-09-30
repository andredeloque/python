numeros = int(input("Digite um numero bem grande: "))
soma = 0
while numeros != 0:
    resto = numeros % 10
    diminuidor = numeros // 10
    numeros = diminuidor
    resultado = resto
    soma = soma + resto
print (soma)
