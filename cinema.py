
# Primero crearemos un dicionario llamado peliculas
# pass Palabra Clave le dice a py que continue
peliculas = {
    "El Padrino":[14,5],
    "El caballero oscuro": [15,6],
    "Pulp Fiction":[12,7],
    "Matrix": [ 7,10],
}

while True:
    eleccion = input("¿Qué película quieres ver?: ").strip().title()
    if eleccion in peliculas:
        edad = int(input("¿Cuántos años tienes?: "))
        if edad >= peliculas[eleccion][0]:
            num_boletos = peliculas[eleccion][1]  # Acceder al segundo elemento de la lista
            if num_boletos > 0:
                print("¡Disfruta tu película!")
                peliculas[eleccion][1] -= 1  # Restar 1 a la cantidad de boletos
            else:
                print("Lo siento, se agotaron los boletos")
        else:
            print("Lo siento, eres muy joven para ver esa película")
    else:
        print("Lo siento, no tenemos esa película")
