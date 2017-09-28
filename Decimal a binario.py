#Decimal a Binario
#Luis Enrique Romero Leyva
numero = int(input("Introduzca el número a convertir: "))
base = 2

def cambio_base(decimal, base):
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion

print ("El número "+str(numero)+" es igual a "+str(cambio_base(numero, base))+" en sistema binario")
