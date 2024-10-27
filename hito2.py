"El usuario introduce un valor (1-Piedra|2- Papel|3-Tijera), si no es correcto se volver a pedir de nuevo hasta que se correcta.La “maquina generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Alfinalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o empatado."
#Importamos el random para luego generar el numero random de la maquina para seleccionar  piedra papel tijeras
import random
usuario_valor = ""
resultado= ""
contador_maquina=0
contador_usuario=0
opciones= ["Piedra", "Papel", "Tijeras"]
#Hacemos un while True para que cuando introduzca 1,2,3 se salga del bucle y si no que siga introduciendo numeros
while contador_usuario != 3 and contador_maquina !=3:
    usuario_valor=int(input("Introduce un numero para estos valores 1-Piedra , 2-Papel ,3-tijera: "))
    maquina_valor=random.randint(1,3)
    if usuario_valor in (1,2,3):
        print(f"Esta es tu opcion: {opciones [usuario_valor - 1]}")
        print(f"Esta es la opcion de la maquina: {opciones [maquina_valor - 1]}")
#Generamos el numero random de la maquina
#Damos el valor en una lista a opciones para luego mostrar tu opcion y la de la maquina
#Añadimos las condiciones con las reglas del piedra papel o tijeras
        if (usuario_valor == maquina_valor):
            resultado = "Has empatado"
        elif (usuario_valor == 1 and maquina_valor == 3):
            resultado = "Has ganado"
            contador_usuario= contador_usuario+1
        elif (usuario_valor == 2 and maquina_valor == 1):
            resultado = "Has ganado"
            contador_usuario= contador_usuario+1
        elif (usuario_valor == 3 and maquina_valor == 2):
            resultado = "Has ganado"
            contador_usuario= contador_usuario+1
        else:
            resultado = "Has perdido"
            contador_maquina= contador_maquina+1
        #Imprimimos el resultado  
        print(f"El resultado es: {resultado}")
    else:
        print(f"Error introduce 1,2 o 3")