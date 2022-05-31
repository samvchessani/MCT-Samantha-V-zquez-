#comentarios: son notas para su yo del futuro

"""hola"""

#print(mensaje): permite mandar informacion a la pantalla
print("hola")

print("saludines")

print(5)

print(5+5)

#constantes son datos que NO CAMBIAN

dia=6

print(dia)

pie=3.1416

print(pie)

#variables son datos que PUEDEN o NO CAMBIAR

calificacion=7

print(calificacion)

calificacion=calificacion+2

print(calificacion)

print("hoy es 4 de enero")

#print mas bonito

print("tu calificacion es: ", calificacion)

print("hoy es ", dia, "de enero")

print(pie, "es el valor de pi que usaremos")

#operadores matematicos
# + suma, -resta, *multp, /division

a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(b/a)

print((a+b)*b)

#jerarquia de operaciones (parentesis, potencias, mult, sumas)

#loop: se refiere a cualquier codigo que se pueda ciclar o repetir un numero de veces

#WHILE: mientras una condicion ocurra (o no) se ejecuta todo el codigo de adentro de la misma

tomate=2

#operadores logicos
#a>b a es mayor que b
#a<b a es menor que b
#a==b a es identico a b

#a>=b a es mayor o igual que b
#a<=b a es menor o igual que b

tomate=2
while(tomate>0):
 print("hay tomate")
 tomate=tomate-1

#identacion y estas nos dice que lineas perteneces a un ciclo o condicion, puede ser un simple espacio o un tab 

#while True es una condicion que pregunta si se puede ejecutar, si respondes que si, el codigo funciona

'''while True:
  print("hola")'''


#input(): nos permite ingresar informacion al codigo desde la consola


#nombre es una variable porque puede cambiar si se ejecuta de nuevo
nombre=input()
print("saludos", nombre)
###########################
apellido=input("apellido: ")
print("saludos mr.", apellido)

edad=input()
print(edad*10)
#input solo recibe STRINGS, necesitas convertirlo si quieres trabajar con numeros

#int() convertir letras a numeros enteros
edad=int(input())
print(edad*10)
