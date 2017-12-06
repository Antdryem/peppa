def residuo(variable):
    print("""
        El resultado es:    
    """)
#aqui calcula e imprime el residuo
    print int(variable[1])%int(variable[2])
    raw_input("presiona Enter para continuar")


def BtH(orden, numero):
#elige en que orden va a hacer la conversion
    if orden=="0":
        largo=len(numero)/4
        sobra=len(numero)%4
        x=0
        resultado=""
        aux=0
#convierte de 4 en 4 cada uno de llos valores 
        while x<largo:
            y=0
       
            if numero[x*4+0]=="0" and numero[x*4+1]=="0" and numero[x*4+2]=="0" and numero[x*4+3]=="0":
                resultado="0"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="0" and numero[x*4+2]=="0" and numero[x*4+3]=="1":
                resultado="1"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="0" and numero[x*4+2]=="1" and numero[x*4+3]=="0":
                resultado="2"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="0" and numero[x*4+2]=="1" and numero[x*4+3]=="1":
                resultado="3"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="1" and numero[x*4+2]=="0" and numero[x*4+3]=="0":
                resultado="4"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="1" and numero[x*4+2]=="0" and numero[x*4+3]=="1":
                resultado="5"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="1" and numero[x*4+2]=="1" and numero[x*4+3]=="0":
                resultado="6"+resultado
            if numero[x*4+0]=="0" and numero[x*4+1]=="1" and numero[x*4+2]=="1" and numero[x*4+3]=="1":
                resultado="7"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="0" and numero[x*4+2]=="0" and numero[x*4+3]=="0":
                resultado="8"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="0" and numero[x*4+2]=="0" and numero[x*4+3]=="1":
                resultado="9"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="0" and numero[x*4+2]=="1" and numero[x*4+3]=="0":
                resultado="A"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="0" and numero[x*4+2]=="1" and numero[x*4+3]=="1":
                resultado="B"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="1" and numero[x*4+2]=="0" and numero[x*4+3]=="0":
                resultado="C"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="1" and numero[x*4+2]=="0" and numero[x*4+3]=="1":
                resultado="D"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="1" and numero[x*4+2]=="1" and numero[x*4+3]=="0":
                resultado="E"+resultado
            if numero[x*4+0]=="1" and numero[x*4+1]=="1" and numero[x*4+2]=="1" and numero[x*4+3]=="1":
                resultado="F"+resultado
            
            x=x+1
#convierte los digitos restantes del numero que se desea convertir
        penelope=""
        x=0
        while x<sobra:
            if numero[(largo-1)+x]=="1":
                penelope="1"+penelope
            else:
                penelope="0"+penelope
            x=x+1

        if penelope=="000":
            resultado="0"+resultado
        if penelope=="001":
            resultado="1"+resultado
        if penelope=="010":
            resultado="2"+resultado
        if penelope=="011":
            resultado="3"+resultado
        if penelope=="100":
            resultado="4"+resultado
        if penelope=="101":
            resultado="5"+resultado
        if penelope=="110":
            resultado="6"+resultado
        if penelope=="111":
            resultado="7"+resultado
        if penelope=="00":
            resultado="0"+resultado
        if penelope=="01":
            resultado="1"+resultado
        if penelope=="10":
            resultado="2"+resultado
        if penelope=="11":
            resultado="3"+resultado
        if penelope=="0":
            resultado="0"+resultado
        if penelope=="1":
            resultado="1"+resultado
    
        print resultado
    else:
#convierte de uno por uno los numeros decimales para pasarlos en binario
        if orden=="1":
            x=0
            salida=""
            while x<len(numero):
                if numero[x]=="0":
                    salida=salida+"0000"
                if numero[x]=="1":
                    salida=salida+"0001"
                if numero[x]=="2":
                    salida=salida+"0010"
                if numero[x]=="3":
                    salida=salida+"0011"
                if numero[x]=="4":
                    salida=salida+"0100"
                if numero[x]=="5":
                    salida=salida+"0101"
                if numero[x]=="6":
                    salida=salida+"0110"
                if numero[x]=="7":
                    salida=salida+"0111"
                if numero[x]=="8":
                    salida=salida+"1000"
                if numero[x]=="9":
                    salida=salida+"1001"
                if numero[x]=="A":
                    salida=salida+"1010"
                if numero[x]=="B":
                    salida=salida+"1011"
                if numero[x]=="C":
                    salida=salida+"1100"
                if numero[x]=="D":
                    salida=salida+"1101"
                if numero[x]=="E":
                    salida=salida+"1110"
                if numero[x]=="F":
                    salida=salida+"1111"

                x=x+1
            print(salida)
        else:
#si se escribio mal el comando saldra esto
            print("No mame compa; 0 para B a H, 1 para H a B")










salir=False



#####     AQUI ACABA LO CHIDO :v



##################shiro

def NP():
    try:
        x=int(raw_input("Introduzca un numero: "))
        contador = 0
        for num in range(1,x+1):                                             #calcula la cantidad de divisores posibles
            if (x % num == 0):
                contador = contador + 1
        if (contador==2):                                                     #si son 2, es primo
            print "El numero "+str(x)+" es primo"
        elif(contador ==1):
            print("Introduzca un numero mayor al 1")                                #si es 1, tiene que haber sido el numero "1"
        else:
            print("El numero "+str(x)+" no es primo")                              #si tiene mas, no es primo
    except ValueError:
        print("sigue participando(no se puede)")                                   #si hubiera crasheado, imprime el mensaje

def DIV():
    try:
        Divisor = int(raw_input("Escribe cuanto vale el divisor "))
        Dividente = int(raw_input("Escribe cuanto vale el dividente "))
        if (Dividente==0):                                                         #evita dividir entre 0
            print("sigue participando (no se puede dividir entre 0)")
        else:
            Resultado = Divisor/Dividente
            print ("El resultado es " + str(Resultado))
    except ValueError:
        print("Input invalido")

def HD():
	A=10
	B=11
	C=12
	D=13
	E=14
	F=15
	lista_permitida=["1","2","3","4","5","6","7","8","9","0","A","B","C","E","F"]                           #define los inputs validos
	lista_letras=["A","B","C","D","E","F"]                                                                  #  "     "    "       "
	lista_hexa=[]
	completo=False
	suma=0
	hexadecimiliador=16
	sumador=0
	comprobar=0
	hexa=raw_input("Ingrese el numero hexadecimal: ").upper()
	contador=int(len(hexa))-1
	while(contador>=0):
	    lista_hexa.append(hexa[contador])
	    contador-=1
	
	while(comprobar<len(lista_hexa)):                                                         #comprueba que el input sea valido
	    if(lista_hexa[comprobar] in lista_permitida):
	        comprobar+=1
	    else:
	        lista_hexa=[]
	        contador=0
	        comprobar=0
	        hexa=raw_input("Ingrese el numero hexadecimal: ").upper()
	        contador=int(len(hexa))-1
	        while(contador>=0):
	            lista_hexa.append(hexa[contador])
	            contador-=1
	
	
	while (sumador<len(lista_hexa)):                                                                #resuelve
	    if(lista_hexa[sumador] in lista_letras):
	        if(lista_hexa[sumador] =="A"):
	            suma+=(A*(hexadecimiliador**sumador))
	        if(lista_hexa[sumador] =="B"):
	            suma+=(B*(hexadecimiliador**sumador))
	        if(lista_hexa[sumador] =="C"):
	            suma+=(C*(hexadecimiliador**sumador))
	        if(lista_hexa[sumador] =="D"):
	            suma+=(D*(hexadecimiliador**sumador))
	        if(lista_hexa[sumador] =="E"):
	            suma+=(E*(hexadecimiliador**sumador))
	        if(lista_hexa[sumador] =="F"):
	            suma+=(F*(hexadecimiliador**sumador))
	    else:
	        suma+=(int(lista_hexa[sumador])*(hexadecimiliador**sumador))
	    sumador+=1
	print""
	print""
	print "El equivalente en decimal es: "+suma


################# luis

#Suma
#Luis Enrique Romero Leyva
def SUM(numeros):
    try:
      numeros=int(raw_input("Cantidad de numeros a sumar: "))
      if numeros==int:
          suma=0
          while numeros>0:
              numero=int(raw_input("Numero a sumar: "))          
              suma=suma+numero                                   
              numeros=numeros-1
              print (suma)
    except ValueError:
        print "Se ha ingresado un caracter no valido, no se puede ejecutar la operacion"
        return
    

#Decimal a Binario
#Luis Enrique Romero Leyva
def BD(numero):
    try:
        numero = int(raw_input("Introduzca el n�mero a convertir: "))   #Introduce el numero que se desea convertir
        base = 2                                                        #Se define que se va a cambiar a base 2 (Binario)

        def cambio_base(decimal, base):                                 #Se define la operaci�n para el cambio de base
            conversion = ''
            while decimal // base != 0:
                conversion = str(decimal % base) + conversion           
                decimal = decimal // base
            return str(decimal) + conversion

        print ("El n�mero "+str(numero)+" es igual a "+str(cambio_base(numero, base))+" en sistema binario")    #Se imprime el resultado de la operaci�n
    except ValueError:
        print "Se ha ingresado un caracter no valido, no se puede ejecutar la operacion"
        return
#Exponente
#Luis Enrique Romero Leyva
def EXP(Valores):
    try:
        Valores=int(raw_input("Introduzca el numero elevar: "))                     #Se ingresa el numero a elevar
        Exponente=int(raw_input("Introduzca el numero a elevar: "))                 #Se ingresa la potencia a la que e quiere elevar
        resultado=Valores**Exponente                                                #Se realiza la operaci�n de elevar el numero a la potencia
        print str(Valores)+" a la "+str(Exponente)+" es igual a "+str(resultado)    #Se imprime el resultado
    except ValueError:
        print "Se ha ingresado un caracter no valido, no se puede ejecutar la operacion"
        return




##########david


def MUL():                                                                 #Multiplicacion
    try:
        print ("Multiplicacion: \n")
        nmul=float(raw_input("Cuantos valores desea multiplicar?"))
        if(nmul < 0):                                                   #impide que se introduzca un numero negativo en "cantidad de numeros a multiplicar"
            print ("Introduzca un numero positivo")
        r=1
        if nmul == 1 :                                                       #se piden al menos dos valores para multiplicar
            print ("Se necesitan al menos dos valores")
            nmul=0
        while(nmul != 0):
            x=float(raw_input("Numero:"))
            r=float(r)*x
            nmul=float(nmul)-1
        print ("El resultado es: ")+str(r)
    except ValueError:                                                   #si va a crashear, escribe "fak u" en vez de crashear
        print ("fak u (operacion imposible)")

def RZ(inp):                                                          #Raices
    try:
        print ("Raices: \n")
        numeros=["1","2","3","4","5","6","7","8","9","0"]
        inp=raw_input("Inserte numero y exponente: ").split()
        n=int(inp[0])
        if(len(inp) == 1):                                     #si se da un exponente, es por default 2
            exp=2
        else:
            exp=int(inp[1])
        if(n >= 0):
            r=""
            if(exp >= 0):
                r=n**(1.0/exp)
                print ("El resultado es: ")+str(r)
            else:
                print("Favor de introducir un exponente positivo")        #evitar operaciones imposibles       |
        elif(n < 0):                                                      #                                    v 
            if(exp % 2 == 0 ):
                print("El resultado es un numero imaginario")             
            else:
                r=""
                if(exp >= 0):
                    print("Favor de introducir un numero positivo")
                else:
                    print("Favor de introducir un exponente positivo")
    
                print ("El resultado es: ")+str(r)
    except ValueError:
        print ("Y yo soy el presidente (operacion imposible)")             #si va a crashear, escribe "Y yo soy el presidente" en vez de crashear

def PRI(input):                                          #numeros primos en un rango definido
    try:
        print "Numeros primos en un rango: \n"
        input= raw_input("Inserte los limites inferior y superior: ").split()
        numero1=int(input[0])
        numero2=int(input[1])
        for x in range(numero1,numero2+1):                                #se calcula en cada numero del rango
            contador = 0
            for num in range(1,x+1):                                       #se calcula si el numero es primo
                if (x % num == 0):
                    contador = contador + 1
            if (contador==2):                                                 #imprime solo los primos
                print "El numero "+str(x)+" es primo"
    except ValueError:
        print("ai laic boterfais (operacion imposible)")                 #si va a crashear, escribe "I like butterflies" en vez de crashear


salir=False;

while not salir:

    print("""
        SUM Funcion de suma
        MUL Funcion de multiplicar
        DIV Funcion de dividir
        RES Funcion de residuo
        EXP Funcion de exponente
        RZ  Funcion de raiz
        BD  Funcion binario-decimal
        BH  Funcion binario-hexadecimal
        HD  Funcion hexadecimal-decimal
        PRI Funcion rango de numeros primos
        NP  Funcion numero primo
        HP  Ayuda sobre funciones
        S   Salir de aplicacion

    """)
    ejecutar=raw_input("""Bienvenido
    """)

    if ejecutar=="S" or ejecutar=="s":
        salir=True
    
    funcion=ejecutar.split(" ")

    if funcion[0]=="RES":
        residuo(funcion)

    if funcion[0]=="BH":
        BtH(funcion[1], funcion[2])

    if funcion[0]=="NP":
        NP(0)

    if funcion[0]=="BD":
        BD(0)

    if funcion[0]=="SUM":
        SUM(0)

    if funcion[0]=="MUL":
        MUL(0)

    if funcion[0]=="RZ":
        RZ(0)

    if funcion[0]=="DIV":
        DIV(0)

    if funcion[0]=="PRI":
        PRI(0)

    if funcion[0]=="EXP":
        EXP(0)
     
    if funcion[0]=="HD":
        EXP(0)
    
