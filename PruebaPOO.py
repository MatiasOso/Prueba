"""Evaluación 1
Para una aplicación similar a uber, crea un programa que solicite los datos para registrar un vehículo, y posteriormente mostrar los datos por pantalla.
Presione 1 para registrarse.
Presione 2 para comenzar una carrera
Al comenzar la carrera, obtendremos varias opciones, para el vehículo.
1.- Ingresar ubicación GPS, LATITUD
2.- Ingresar ubicación GPS, LONGITUD
3.- Encender el vehículo.
4.- Acelerar vehículo
5.- Apagar Vehículo
6.- Girar Vehículo
Al acelerar el vehículo, entonces su velocidad se incrementará en 10 km/h
Usted está viajando a 10 Km/h
al presionar nuevamente acelerar, arrojará
Usted está viajando a 20 Km/h
utilizando la función Date, podríamos obtener la fecha / hora.
Al finalizar la carrera, entonces se deberá ingresar la ubicación GPS, del destino.
Calcula la distancia recorrida, con los datos obtenidos anteriormente. Debes mostrar cuál es el total a pagar por dicha carrera.
Realiza el envío del código fuente por medio de la intranet, y adicionalmente, en un archivo llamado repo.txt, agrega la URL del repositorio GIT, en donde se encuentra el proyecto."""


from ast import Str


registro=False
while registro==False:
    print("Bienvenido, Por favor Registrese")
    nombre= str(input("Ingrese su nombre y apellido: "))
    telefono = int(input("Ingrese su numero de telefono: "))
    correo = str(input("Ingrese su correo electronico: "))
    auto= str(input("Ingrese el modelo de su vehiculo: "))
    placa= str(input("Ingrese la placa de su vehiculo: "))
    print("Bienvenido", nombre, "su numero de telefono es:", telefono, "su correo electronico es:", correo)
    print("Su vehiculo es un", auto, "con placa", placa)
    registro=True
print("Presione 1 para comenzar una carrera")
print("Presione 2 para salir")
opcion = int(input("Ingrese una opcion: "))
if opcion == 1:
    print("1.- Ingresar ubicación GPS, LATITUD")
    latitud = int(input("Ingrese la latitud: "))
    print("La latitud es:", latitud)
        
    print("2.- Ingresar ubicación GPS, LONGITUD")
    longitud = int(input("Ingrese la longitud: "))
    print("La longitud es:", longitud)

    print("Presione 1 para encencer el vehiculo y 2 para apagarlo")
    opc= int(input("Ingrese una opcion: "))
    velocidad = 10
    while opc == 1 or opc== 3 or opc==4 or opc==5:
  
        print("Usted esta viajando a",velocidad ,"Km/h")
        print ("Presiona 3 para acelerar ,4 para frenar , 5 para girar y 2 para terminar el viaje")
        opc=int(input())
        if opc == 3:
            velocidad = velocidad + 10
        elif opc == 4:
            velocidad = velocidad - 10
        elif opc == 5:
            print("Usted esta girando, redujo su velocidad a 10 Km/h")
        elif opc == 2:
            print("El vehiculo esta apagado")
            velocidad = 0
            break
        else:
            print("Opcion no valida")
            break
    print("Ingrese la latitud de su destino")
    latitud2 = input("Ingrese la latitud: ")
    print("La latitud es:", latitud2)
    print("Ingrese la longitud de su destino")
    longitud2 = input("Ingrese la longitud: ")
    print("La longitud es:", longitud2)
    distancia = ((float(latitud2)-float(latitud))**2+(float(longitud2)-float(longitud))**2)**0.5
    print("La distancia recorrida es:", distancia)
    print("El total a pagar es:", distancia*1000)
elif opcion == 2:
    print("Gracias por usar Uber")

else:
    print("Opcion no valida")
