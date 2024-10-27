'''CUESTION 3: Simular el funcionamiento de una cuenta bancaria : al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto. 
Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos. 
'''
saldo=-1
contador_ingreso=0
contador_retirada=0
opciones=""
#Generamos un while para obligar a que el saldo sea positivo
while saldo <0:
    saldo = float(input("Introduce el saldo inicial de la cuenta: "))

#Generamos otro while para que las opciones sea desigual a 5

while opciones != 5 :
    opciones = int(input("Menu : 1- Ingresar dinero, 2- Retirar dinero, 3- Mostrar el saldo, 4- Estadisticas y 5 salir: "))
    #Generamos una lista con todas las opciones
    if opciones in [1, 2, 3, 4, 5]:
        #Ponemos la opcion 1 generamos dinero_ingresado para que el usuario pueda ingresar dinero con el float para que pueda haber decimales y ponemos que si el saldo es mayor a 0 que se sume al saldo y el contador de ingresos sube a 1 por que ha realizado un movimiento
        if opciones == 1:
            while True:
                dinero_ingresado=float(input("Que cantidad vas a ingresar?: "))
                if dinero_ingresado > 0:
                    saldo = saldo+dinero_ingresado
                    contador_ingreso=contador_ingreso+1
                    break
                else:
                    print("Cantidad incorrecta")
        #Ponemos la opcion 2 generamos dinero_retirado para que el usuario pueda retirarº dinero con el float para que pueda haber decimales y ponemos que si el saldo es mayor o igual a 0 y que si el dinero retirado es menor o igual al saldo que se reste el dinero retirado del saldo y que el contador de retirada sume 1 por que ha realizado un movimiento
        if opciones == 2:
            while True:
                dinero_retirado=float(input("Que cantidad vas a retirar?: "))
                if dinero_retirado >= 0:
                    if dinero_retirado <=saldo:
                        saldo=saldo-dinero_retirado
                        contador_retirada=contador_retirada+1
                        break
                    else:
                        print("No puedes retirar mas cantidad de la que tienes")
                else:
                    print("Cantidad no valida")
        #Si la opcion es 3 se muestra el saldo
        if opciones == 3:
            print(f"El saldo que tienes es {saldo} ")
        #Si la opcion es 4 se muestran los contadores de los ingresos y de las retiradas
        if opciones == 4:
            print (f"Has ingresado un total de veces de {contador_ingreso}")
            print(f"Has retirado un total de veces de {contador_retirada}")
        #Si la opcion es la 5 se sale
        if opciones ==5:
            print("Salir")
    #Este else funciona para el primer while para introducir un numero valido
    else:
        print("El numero no es valido")
