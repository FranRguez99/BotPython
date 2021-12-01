import re
import json
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


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
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
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
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        comprobarentrada(entrada)


# Funciones Bot Regex a partir de ficheros
def escribirRespuesta(respuesta):
    guardarEnRegistro(respuesta)
    print(f'\t\t>{respuesta}')


def guardarEnRegistro(texto):
    with open("conversacion.txt", "a") as registro:
        registro.writelines(f"\t\t>{texto}\n")


def cadenapatron(delpatron, delacadena):
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena


def botRegexFichero():
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
    with open("respuestas.json") as ficheroJSON:
        jsonDiccionario = json.load(ficheroJSON)
        with open("conversacion.txt", "w"):
            pass
        listaValores = jsonDiccionario["ListaValores"]
        opcionSalir = jsonDiccionario["opcionSalir"]
        noSabeRespuesta = jsonDiccionario["noSabeRespuesta"]

    salir = False
    while not salir:
        conoceValor = False
        datosUsuario = input("\t\t>")
        guardarEnRegistro(datosUsuario)
        for opcion in opcionSalir:
            if datosUsuario.casefold() == opcion:
                salir = True
        if not salir:
            for valores in listaValores:
                regex = re.compile(valores[0], re.IGNORECASE)
                if re.search(regex, datosUsuario):
                    variable = cadpatr(regex, datosUsuario)
                    respuesta = valores[1].replace("{variable}", variable).replace("?", "")
                    conoceValor = True
                    escribirRespuesta(respuesta)
                    break
            if not conoceValor:
                escribirRespuesta(noSabeRespuesta)


# Funciones ReportLab
def crearpdf():
    pdf = 'chat.pdf'
    can = canvas.Canvas(pdf)
    can.drawImage('chatbot_python.jpg', 120, 600, width=350, height=175)
    can.setFont('Helvetica-Bold', 21)
    can.drawString(122, 578, 'INFORME DE LA CONVERSACIÓN')
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    conversacion = can.beginText(95, 524)
    conversacion.setFont("Times-Roman", 12)
    for linea in lista_texto:
        conversacion.textLine(linea.replace("\n", "").replace("\t", ""))
    can.drawText(conversacion)
    funciones = can.beginText(95, conversacion.getY()-20)
    funciones.setFont("Times-Roman", 12)
    funciones.textLine(f'La conversación es del {fecha()}')
    funciones.textLine()
    funciones.textLine(f'Consta de {cuentaCaracteres()} caracteres.')
    funciones.textLine()
    funciones.textLine(f'Está compuesta por {cuentaPalabras()} palabras.')
    funciones.textLine()
    funciones.textLine(f'La palabra de aparece {cuentaDe()} veces.')
    can.drawText(funciones)
    can.save()


def fecha():
    return str(datetime.today().strftime('%Y-%m-%d'))


def cuentaCaracteres():
    suma = 0
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    for linea in lista_texto:
        suma += len(linea.replace(" ", "").replace(">", "").replace("\n", "").replace("\t", ""))
    return suma


def cuentaPalabras():
    suma = 0
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    for linea in lista_texto:
        suma += len(linea.split())
    return suma


def cuentaDe():
    suma = 0
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    for linea in lista_texto:
        palabras = linea.replace(".", "").replace(",", "").split()
        for palabra in palabras:
            if palabra == 'de':
                suma += 1
    return suma

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
    elif opcion == 2:
        botRegex()
    elif opcion == 3:
        botRegexFichero()
    elif opcion == 4:
        crearpdf()
    elif opcion == 5:
        salir = True
    else:
        print('Introduzca un número del 1 al 5')
