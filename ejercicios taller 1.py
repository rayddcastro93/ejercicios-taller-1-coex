#taller numero 1
#x = int(input("¿Cuál es el primer número?")) #Preguntamos al usuario qué número quiere
#y = int(input("¿Cuál es el segundo número?"))
#z = int(input("¿Cuál es el tercer15 número?"))
#if x>y
#  print('El primer número es mayor.')
#    if x>z
#elif x<y:
#  print('El primer número es menor.')
#else:
#  print('Es el mismo número.')
# me falta el comparador de numero con 3 numeros distintos

#EJERCICO DE TALLER CON OPERANDOS 1

# 40 + 2 * 7 ^ 2
#EJEMPLO1 = (40+2*7**2)
#print(EJEMPLO1)
# 3+ (2+5)*1+ (3-2*3)
#EJEMPLO2 = ( 3+(2+5)*1+(3-2*3))
#print(EJEMPLO2)
# 16 - 8 * (10 - (5 + 4))
#EJEMPLO3 =(16-8*(10-(5+4)))
#print (EJEMPLO3)
#(5+3*2)-(7*2)*(3+ (2*3-1))
#EJEMPLO4 =(5+3*2)-(7*2)*(3+ (2*3-1))
#print(EJEMPLO4)
# 24+220)/3*2
#EJEMPLO5 =(24-220)/3*2
#print(EJEMPLO5)
# (6/3*2)-(7*2)+ (2*(3+ (2/3-1)*4))
#EJEMPLO6 =(6/3*2)-(7*2)+ (2*(3+ (2/3-1)*4))
#print(EJEMPLO6)

#PARTE 2 DEL TALLER 1 
#A = 29.7 + 5.0 **2.0
#B = ( (2 - 3) ** 4 * 5 / (4 + 3 * 9) )
#C = 49.38 + 127.73 - 15.02 * 6.83 / 3.22
#D = 19 % 3
#E = 15 % 6
#F = ((15 * 8 % 6 + 24 / 2**3)**3 / 4) * (5 **1 / 2 + 1 / 4 + 2 ** 3 -4)
#print(A,B,C,D,E,F)

#TALLER 2 

#Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta
#lo siguiente:
#• toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
#• cada minuto adicional a partir de los tres primeros es un paso de contador y
#cuesta 100 pesos
#Pedir al usuario la duración de la llamada en minutos

#duracion = int(input("Ingrese la duración de la llamada en minutos: "))

#Calcular el costo total de la llamada
#if duracion <= 3:
#    costo_total = 200
#else:
#    costo_total = 200 + (duracion - 3) * 100

 #Imprimir el resultado
 
#print("El costo total de la llamada es de ", costo_total, " pesos.")
#*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros
#             y Y conejos blancos. Hacer un algoritmo que:
#• Imprima la cantidad de conejos vendida
#• Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de
#             los conejos negros, imprima el monto total de la venta.
#• Imprima el color de los conejos que se vendieron más.
#/*/*/*/*/*/*/*/*/*/*/***/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/
# se le piden los datos de los conejos al cliente
#print("Bienvenido porfavor ingresa  cuantos conejos blancos y negros has vendido")
# ingresa cuantos conejos blancos y negros ha vendido 
#C1 = int(input("(¿cuantos conejos blancos vendiste?"))
#C2 = int(input("(cuantos conejos negros vendiste?"))
# se indica a l usuario cuantos conejos se vendieron en total 
#C3 = (C1 + C2)
#print ("Cantidad de conejos vendidos total",C3)
 #se solicita el valor de los conejos blancos y negros 
#P1 = float(input(" dime a como vendiste cada conejo blanco"))
#P2 = float(input("dime a como vendiste cada conejos negros")) 

#Total = ((P1*C1)+(P2*C2))
# valor o monto ganado 
#print("Monto ganado es:",Total,"pesos")

#if C1>C2:
#    print("se vendieron mas conejos blancos ",C1)
#elif C1==C2:
#  print("se vendieron la misma cantidad de conejos",C1,C2)
#else:
#print("se vendieron mas conejos negro",C2)
#*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

#6. Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes,
#determinadas sobre las siguientes condiciones:
#• NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante
#tendrá 3 evaluaciones.
#• NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante
#presentara 2 trabajos.
#• NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
#• Nota mínima 1,0 nota máxima: 5,0


#print ("hola , bienvenido a su calculadora de notas" )

#print("vamos a empezar por sus notas de sus evaluaciones,recuerde solo son 3 y valen el 60% de la nota final")
#notaN01 = float(input("nota de la primera evaluacion?  "))
#NotaN02 = float(input("nota de la segunda evaluacion?  "))
#notaN03 = float(input("nota de la tercera evaluacion?  "))

#Nota60 = ((notaN01+notaN03+NotaN02)/3)*0.6

#print("porfavor ingresar las notas de tus trabajos")

#notatra1 = float(input("ingresa la nota de tu primer trabajo?  "))
#notatra2 = float(input("ingresa la nota de tu segunda trabajo?  "))

#Nota40 = ((notatra1+notatra2)/2)*0.4

#Final = (Nota40 + Nota60)

#print( "su nota final para este curso es de ",Final)

#/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*


#Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,
#cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
#clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo
#existen dos claves).

#print(" Bienvenido a supermercasdos babiera , porfavor a continuacion dime que articulos vas a llevar .")

#print("a continuacion indicame que vas a llevar ,sean frutas,verduras,carnes o miselaneos recuerda ingresar el valor de tu articulo. Gracias ")

#elem   =str(input("porfavor dime que vas a llevar ?"))
#precio =float(input("indicame el valor del articulo,gracias"))

#print("a continuacion indicame tu tiket de descuerto")

#des10 = 1
#des20 = 2

#descuento = float(input("ingresa tu codigo de descuento,gracias"))

#if descuento == des10:
#    print("El valor de tu factura recibe un 10%  de descuento", valordesc,"de tus articulos",elem,"precio original",precio)
#    valordesc=((precio*0.1)-(precio))
#elif descuento == des20:
#    valordesc=((precio*0.2)-(precio))
#    print("El valor de tu factura recibe un 20% de descuento", valordesc,"de tus articulos",elem,"precio original",precio)
    
#else :
#  print ("El valor de tu compra no recibe descuento pues no usaste el cupón",precio,"de tu articulo",elem)
#print("Feliz dia y vuelva pronto")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología. El
#presupuesto anual del hospital se reparte a estas tres (3) áreas; usted debe realizar
#un algoritmo que permita ingresar el valor del presupuesto anual, ingresar el
#porcentaje correspondiente a cada área, realizar el cálculo del presupuesto que
#corresponde a cada área,si la suma de los porcentajes no corresponde al 100% debe
#mostrar un mensaje de error.
#Mostrar el porcentaje asignado a cada área y el presupuesto obtenido.


# Pedimos al usuario que ingrese el presupuesto anual

#presupuesto_anual = float(input("Ingrese el presupuesto anual: "))

# Pedimos al usuario que ingrese los porcentajes correspondientes a cada área
#porcentaje_psiquiatria = float(input("Ingrese el porcentaje para Psiquiatría: "))
#porcentaje_pediatría = float(input("Ingrese el porcentaje para Pediatría: "))
#porcentaje_traumatologia = float(input("Ingrese el porcentaje para Traumatología: "))

# Verificamos que la suma de los porcentajes sea igual a 100%
#suma_porcentajes = porcentaje_psiquiatria + porcentaje_pediatría + porcentaje_traumatologia
#if suma_porcentajes != 100:
#    print("Error: La suma de los porcentajes no es igual a 100%")
#else:
#    # Calculamos el presupuesto para cada área
#    presupuesto_psiquiatria = presupuesto_anual * porcentaje_psiquiatria / 100
#    presupuesto_pediatría = presupuesto_anual * porcentaje_pediatría / 100
#    presupuesto_traumatologia = presupuesto_anual * porcentaje_traumatologia / 100

    # Mostramos los resultados
#    print("Porcentaje asignado a Psiquiatría:", porcentaje_psiquiatria)
#    print("Presupuesto asignado a Psiquiatría:", presupuesto_psiquiatria)
#    print("Porcentaje asignado a Pediatría:", porcentaje_pediatría)
#    print("Presupuesto asignado a Pediatría:", presupuesto_pediatría)
#    print("Porcentaje asignado a Traumatología:", porcentaje_traumatologia)
#    print("Presupuesto asignado a Traumatología:", presupuesto_traumatologia)


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

#Diseñar un algoritmo para determinar el precio del tiquete de ida y vuelta en avión,
#conociendo la distancia a recorrer, sabiendo que si el número de días de estancia es
#superior o igual a 7 y la distancia superior a 800 km el billete tiene una reducción
#del30%. El precio por km es de $2,5 dólares.

print("Hola bienvenido a tu proximo vuelo,porfavor a continuacion ingresa los datos requeridos a continuacion ")


disvuel= print(str(input("porfavor dame la distancia del vuelo ")))

disvuel2dias = print(str(input("porfavor dime cuanto tiempo te piensas quedar")))











#Diseñar un algoritmo que lea por teclado un número
#comprendido entre 1 y 10. Se desea visualizarsi el número es par o impar. En primer
#lugar, se deberá
#detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
#si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”;si es 2, 4, 6, 8, 10, escribir
#un mensaje de “par”.

num = int(input("introdusca numeros del 1 al 10 "))

match num:
    case 1 :
        print ("el numero es inpar")
    case 3:
        print ("el numero es inpar")
    case 5:    
        print ("el numero es inpar")
    case 7:
        print ("el numero es inpar")
    case 9:
        print ("el numero es inpar")
            
    case 2:
        print("el numero es par ")
    case 4:
        print("el numero es par")
    case 6:
        print("el numero es par")
    case 8:
        print("el numero es par ") 
    case 10:
        print("el numero es par")   
    case other:
        print("el numero es invalido o fuera del rango")

#Diseñar un algoritmo que lea un número entero entre 1 y 10, y
#nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído
#no está comprendido entre 1 y 10 mostrar un mensaje de error.


#Diseñar un algoritmo que lea por teclado un número
#comprendido entre 1 y 10. Se desea visualizarsi el número es par o impar. En primer
#lugar, se deberá
#detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
#si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”;si es 2, 4, 6, 8, 10, escribir
#un mensaje de “par”.

#num = int(input("introdusca numeros del 1 al 10 "))

        #match num:
        #    case 1 :
        #        print ("el numero es inpar")
        #    case 3:
        #        print ("el numero es inpar")
        #    case 5:    
        #        print ("el numero es inpar")
        #    case 7:
        #        print ("el numero es inpar")
        #    case 9:
        #        print ("el numero es inpar")
                    
        #    case 2:
        #        print("el numero es par ")
        #    case 4:
        #        print("el numero es par")
        #    case 6:
        #        print("el numero es par")
        #    case 8:
        #        print("el numero es par ") 
        #    case 10:
        #        print("el numero es par")   
        #    case other:
        #        print("el numero es invalido o fuera del rango")




        #Diseñar un algoritmo que lea un número entero entre 1 y 10, y
        #nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído
        #no está comprendido entre 1 y 10 mostrar un mensaje de error.

num = int(input("ingrese valores de 1 al 10  "))

match num:

   case 1 :
        print ("UNO")
   case 2:
         print("DOS") 
   case 3 : 
        print ("TRES")
   case 4 :
        print ("CUATRO")
   case 5 :
        print("CINCO") 
   case 6 : 
        print ("SEIS")
   case 7 :
    print ("SIETE")
   case 8 :
    print("OCHO") 
   case 9 : 
    print ("NUEVE")
   case 10 :
     print ("DIEZ")

   case other:
      print("el numero es invalido o fuera del rango")                              