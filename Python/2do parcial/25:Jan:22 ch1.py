# codigo infinito, recibe 3 calificaciones,  calcula promedio, te dice si pasas, repruebas, mayor igual que nueve gana medalla 
while True:
 g1=int(input("Enter your grade"))
 g2=int(input("Enter your second grade"))
 g3=int(input("Enter your third grade"))

 promedio=(g1+g2+g3)/3

 print(("Your final average is, ", promedio))

 if (promedio<6):
    print("You failed")

 if (promedio>=6):
    print("You pass")

 if (promedio>= 9):
    print("You won a medal")