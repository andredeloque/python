segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
print (segundos)
horas = segundos // 3600
segundosRestantes = segundos %3600
minutos = segundosRestantes // 60
finalSegundos = segundosRestantes % 60
dias = horas // 1440
finalMinutos = dias // horas
print ("dias",dias,"horas", horas, "minutos",finalMinutos, "segundos",finalSegundos)


