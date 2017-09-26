# peppa

print ("Multiplicacion: \n")
n=float(input("Cuantos valores desea multiplicar?"))
r=1
if n == 1 :
    print ("Se necesitan al menos dos valores")
    n=0
while(n != 0):
    x=float(input(""))
    r=float(r)*x
    n=float(n)-1
print ("El resultado es: ")+str(r)
