import datetime

dia= datetime.date.today()

print(dia)

w=dia.weekday()+1

print(w)

if(w==0):
  print("feliz domingo")

elif(w==2):
  print("wuhu es martes")

elif(w==1):
  print("f es lunes :(")

elif(w==3):
  print("yei es miercoles")
  
elif(w==4):
  print("juevebesssss, ntc pero si")

elif(w==5):
  print("last day of school!")
  
else:
  print("yahoo, es sabado")

