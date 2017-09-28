#Suma
#Luis Enrique Romero Leyva
numeros=int(input("Cantidad de numeros a sumar: "))
suma=0
while numeros>0:
    numero=int(input("Numero a sumar: "))
    suma=suma+numero
    numeros=numeros-1
print (suma)