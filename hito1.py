"A través de un menú solicitaremos alusuario que tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no escorrecta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta.  Si ha seleccionada un cuadrado, pediremos su lado y mostraremos la figura, su área yperímetroSi ha seleccionada un rectángulo, pediremos base y altura y mostraremos la figura, su área y perímetro"


menu=""

#Creamos un bucle while true para que sea infinito y acabar cuando queramos 
while True:
    menu = int(input("Mostrar menu : 1-Cuadrado 2-Rectangulo y 3-Salir: "))
#Seleccionamos el menu 2 para generar las formulas del rectangulo y su figura
    if menu == 1:
        lado = int(input("Dime el lado del cuadrado: "))
        print(f"EL area del cuadrado es {lado * lado }")
        print(f"El perimetro es {(lado *4)}")
        for asterisco in range (lado):
            print("*" * lado)
#Seleccionamos el menu 2 para generar las formulas del rectangulo y su figura
    elif menu == 2:
        base = int(input("Dime la base del rectagulo: "))
        altura = int(input("Dime la altura del rectangulo: "))
        print (f"El area del rectangulo es {base * altura}")
        print (f"El area del perimetro es {base*2 + altura*2}")
        for i in range (altura):
            print (f"*" * base)
#Seleccionamos el menu 3 para salirnos del bucle while
    elif menu == 3:
        print("Salir")
        break 
    else :
        print ("Error introduce un numero valido: ")