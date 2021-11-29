import re
import json


# Funcion Bot simple
def botSimple():
    diccfrases = {
        "¿Qué tal?": "Bien",
        "Hola": "Muy buenas, usuario. Soy Botarate",
        "¿Qué sabes de animales?": "Mi animal favorito es el orangután",
        "¿Qué sabes de videojuegos?": "Me encanta mortal kombat lo juego 24/7",
        "¿Qué sabes de Anime?": "El viaje de chihiro es una gran película",
        "¿Dónde estamos?": "En la calle calatrava en el SAFA",
        "¿Qué haces ahora?": "Ahora mismo estoy respondiendote a ti y me siento bastante bien",
        "¿Qué hiciste ayer?": "Ayer repartí el oro del mundo como Robin Hood",
        "Adiós": "Adios",

        "Alt": "Lo siento no te he entendido"}
    frase = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    while frase.casefold() != "salir".casefold():
        frase = input("\t\t>")
        if frase in diccfrases:
            print("\t\t>", diccfrases.get(frase))
        elif frase.casefold() == "salir":
            print("\t\t")
        else:
            print("\t\t", diccfrases.get("Alt"))

# Funciones Bot Regex
def cadpatr(delpatron, delacadena):
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena


def comprobarentrada(cadena):
    patroninicio = re.compile(r"^(Hola)(,?)( *soy )", re.IGNORECASE)
    patroncomida = re.compile(r"([¿]?Te gustan )\w+|(^[¿]*Has probado )\w+", re.IGNORECASE)
    patronjuego = re.compile(r"([¿]? *Sabes jugar )\w+|(^[¿]*Has jugado )\w+", re.IGNORECASE)
    patronviaje = re.compile(r"([¿]? *Te gustó ir )\w+|(^[¿]*Has viajado a )\w+", re.IGNORECASE)
    patronequipo = re.compile(r"([¿]? *Tu equipo favorito es el )\w+|(^[¿])\w+", re.IGNORECASE)

    if re.search(patroninicio, cadena):
        nombre = cadpatr(patroninicio, cadena)
        print(f"\t\tMuy buenas, {nombre}. Soy Botarate")

    elif re.search(patroncomida, cadena):
        comida = cadpatr(patroncomida, cadena).replace("?", "")
        print(f"\t\tY a quien no, {comida} me fascinan ")

    elif re.search(patronjuego, cadena):
        juego = cadpatr(patronjuego, cadena).replace("?", "")
        print(f"\t\tPues si, cuando juego {juego} me divierte mucho ")

    elif re.search(patronviaje, cadena):
        viajar = cadpatr(patronviaje, cadena).replace("?", "")
        print(f"\t\tIr a {viajar} ha sido una gran experiencia ")

    elif re.search(patronequipo, cadena):
        equipo = cadpatr(patronequipo, cadena).replace("?", "")
        print(f"\t\tSer del {equipo} es lo mejor que te puede pasar ")
    elif cadena.casefold() == "salir":
        return
    else:
        print("\t\tPues la verdad de eso poco.")


def botRegex():
    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t> ")
        comprobarentrada(entrada)


# Funciones Bot Regex a partir de ficheros
def escribirRespuesta(respuesta, registro):
    guardarEnRegistro(respuesta, registro)
    print(respuesta)


def guardarEnRegistro(texto, registro):
    registro.write(texto)


def cadenapatron(delpatron, delacadena):
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena


def botRegexFichero():
    with open("respuestas.json") as ficheroJSON:
        jsonDiccionario = json.load(ficheroJSON)
        with open("registro.txt", "a") as registro:
            listaValores = jsonDiccionario["ListaValores"]
            opcionSalir = jsonDiccionario["opcionSalir"]
            noSabeRespuesta = jsonDiccionario["noSabeRespuesta"]

            salir = False
            while not salir:
                conoceValor = False
                datosUsuario = input()
                guardarEnRegistro(datosUsuario, registro)
                for opcion in opcionSalir:
                    if datosUsuario.casefold() == opcion:
                        salir = True
                if not salir:
                    for valores in listaValores:
                        regex = re.compile(valores[0], re.IGNORECASE)
                        if re.search(regex, datosUsuario):
                            variable = cadenapatron(regex, datosUsuario)
                            respuesta = valores[1].replace("{variable}", variable).replace("?", "")
                            conoceValor = True
                            escribirRespuesta(respuesta, registro)
                            break
                    if not conoceValor:
                        escribirRespuesta(noSabeRespuesta, registro)

            guardarEnRegistro("#### Conversacion terminada ####", registro)


print('\t\t\t\t\t \033[1m\033[4mAPLICACIÓN BOT-ARATE\033[0m')

salir = False

while not salir:
    print("\n\t\t\t\t\t\t\t\033[1mMenú de Opciones")
    print("\t\t\t\t\t\t\t================\033[0m\n")
    print("\t\t\t1) Bot simple (respuestas planas...)")
    print("\t\t\t2) Bot simple (respuestas REGEX)")
    print("\t\t\t3) Bot simple mejorado desde fichero")
    print("\t\t\t4) Informe de la conversación (PDF)")
    print("\t\t\t5) Salir")
    opcion = int(input("\n\t\t\t\t\t\t\033[1mOpción : \033[0m"))

    if opcion == 1:
        botSimple()
    if opcion == 2:
        botRegex()
    if opcion == 3:
        botRegexFichero()
    if opcion == 4:
        print("PDF")
        # Función del PDF aquí
    if opcion == 5:
        salir = True
    else:
        print('Introduzca un número del 1 al 5')