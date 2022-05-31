#convertir la edad en meses, semanas, dias, horas, minutos y segundos

años=int(input("ingrese su edad:"))
meses=(años*12)
print("tu edad en semanas :", meses)

semanas=(meses*4)
print("tu edad en semanas:",semanas)

dias=(semanas*7)
print("tu edad en dias:", dias)

horas=(dias*24)
print("tu edad en horas:", horas)

minutos=(horas*60)
print("tu edad en minutos", minutos)

segundos=(minutos*60)
print("tu edad en segundos", segundos)