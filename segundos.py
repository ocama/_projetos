segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total = int(segundos)

dias = total // 86400
restantes_horas = total % 86400
horas = restantes_horas // 3600
restantes = total % 3600
minutos = restantes // 60
final = restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", final, "segundos.")
