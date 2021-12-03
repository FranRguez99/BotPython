import re
import json
from datetime import datetime
from reportlab.pdfgen import canvas


# Función Bot simple
def botSimple():
    # Diccionario con los conjuntos de preguntas y respuestas del bot simple
    diccfrases = {
        "¿Qué tal?": "Muy bien, gracias por preguntar",
        "Hola": "Muy buenas, usuario. Soy Botarate",
        "¿Qué sabes de animales?": "Mi animal favorito es el orangután",
        "¿Qué sabes de videojuegos?": "Me encanta mortal kombat lo juego 24/7",
        "¿Qué sabes de anime?": "El viaje de chihiro es una gran película",
        "¿Dónde estamos?": "En la calle calatrava en el SAFA",
        "¿Qué haces ahora?": "Ahora mismo estoy respondiendote a ti y me siento bastante bien",
        "¿Qué hiciste ayer?": "Ayer repartí el oro del mundo como Robin Hood",
        "Adiós": "Adios",

        "Alt": "Lo siento no te he entendido"}
    frase = ""
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
    # Detecta las entradas por teclado del usuario y devuelve la respuesta adecuada o sale
    while frase.casefold() != "salir".casefold():
        frase = input("\t\t>")
        if frase in diccfrases:
            print(f'\t\t>{diccfrases.get(frase)}')
        elif frase.casefold() == "salir":
            print("\t\t")
        else:
            print(f'\t\t>{diccfrases.get("Alt")}')


# Funciones Bot Regex
def cadpatr(delpatron, delacadena):
    # Procesa la cadena introducida para extraer el dato otorgado por el usuario
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena


def comprobarentrada(cadena):
    # Patrones REGEX utilizados en el bot
    patroninicio = re.compile(r"^(Hola)(,?)( *soy )", re.IGNORECASE)
    patroncomida = re.compile(r"([¿]?Te gustan )\w+|(^[¿]*Has probado )\w+", re.IGNORECASE)
    patronjuego = re.compile(r"([¿]? *Sabes jugar )\w+|(^[¿]*Has jugado )\w+", re.IGNORECASE)
    patronviaje = re.compile(r"([¿]? *Te gustó ir )\w+|(^[¿]*Has viajado a )\w+", re.IGNORECASE)
    patronequipo = re.compile(r"([¿]? *Tu equipo favorito es el )\w+|(^[¿])\w+", re.IGNORECASE)
    respuestaSalida = ['salir', 'adios', 'hasta luego']
    # Compara la cadena recibida con los diferentes patrones disponibles para devolver su respuesta
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
    elif cadena.casefold() in respuestaSalida:
        return
    else:
        print("\t\tPues la verdad de eso poco.")


def botRegex():
    entrada = ""
    respuestaSalida = ['salir', 'adios', 'hasta luego']
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
    # Mantiene el bot a la escucha hasta que el usuario indique 'salir'
    while entrada.casefold() not in respuestaSalida:
        entrada = input("\t\t>")
        comprobarentrada(entrada)


# Funciones Bot Regex a partir de ficheros
def escribirRespuesta(respuesta):
    # Escribe las respuestas dentro de nuestro fichero de texto
    guardarEnRegistro(respuesta)
    # Imprime las respuestas por pantalla
    print(f'\t\t>{respuesta}')


def guardarEnRegistro(texto):
    # Guarda la conversación en el fichero
    with open("conversacion.txt", "a") as registro:
        registro.writelines(f"\t\t>{texto}\n")


def cadenapatron(delpatron, delacadena):
    # Extrae el dato introducido por el usuario
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena


def botRegexFichero():
    print("\t\t\033[1mBot a la escucha...(pregunta cuando quieras)\033[0m\n")
    # Apertura de un fichero JSON en el que se encuentran los patrones del bot
    with open("respuestas.json") as ficheroJSON:
        jsonDiccionario = json.load(ficheroJSON)
        with open("conversacion.txt", "w"):
            pass
        listaValores = jsonDiccionario["ListaValores"]
        opcionSalir = jsonDiccionario["opcionSalir"]
        noSabeRespuesta = jsonDiccionario["noSabeRespuesta"]
    # Mantiene el bot a la escucha hasta que se le indique salir y procesa las cadenas introducidas
    salir = False
    while not salir:
        conoceValor = False
        datosUsuario = input("\t\t>")
        for opcion in opcionSalir:
            if datosUsuario.casefold() == opcion:
                salir = True
        if not salir:
            guardarEnRegistro(datosUsuario)
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
    # Escribimos la cabecera en el PDF
    can.drawImage('chatbot_python.jpg', 120, 600, width=350, height=175)
    can.setFont('Helvetica-Bold', 21)
    can.drawString(122, 578, 'INFORME DE LA CONVERSACIÓN')
    # Extraemos la conversación de nuestro fichero
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    can.setFont("Times-Roman", 12)
    y = 530
    numPag = 1
    can.drawString(500, 40, f'Page {numPag}')
    # Bucle que escribe la conversación línea por línea
    for linea in lista_texto:
        if y >= 50:
            can.drawString(95, y, linea.replace("\n", "").replace("\t", ""))
            y = y - 12
        else:
            y = 750
            numPag = numPag + 1
            can.showPage()
            can.drawString(500, 40, f'Page {numPag}')
    y = y - 20
    # Ejecutamos y escribimos las funciones
    if y >= 50:
        can.drawString(95, y, f'La conversación es del {fecha()}')
        y = y - 30
    else:
        y = 750
        numPag = numPag + 1
        can.showPage()
        can.drawString(500, 40, f'Page {numPag}')
    if y >= 50:
        can.drawString(95, y, f'Consta de {cuentaCaracteres()} caracteres.')
        y = y - 30
    else:
        y = 750
        numPag = numPag + 1
        can.showPage()
        can.drawString(500, 40, f'Page {numPag}')
    if y >= 50:
        can.drawString(95, y, f'Está compuesta por {cuentaPalabras()} palabras.')
        y = y - 30
    else:
        y = 750
        numPag = numPag + 1
        can.showPage()
        can.drawString(500, 40, f'Page {numPag}')
    if y >= 50:
        can.drawString(95, y, f'La palabra de aparece {cuentaDe()} veces.')
        y = y - 30
    else:
        y = 750
        numPag = numPag + 1
        can.showPage()
        can.drawString(500, 40, f'Page {numPag}')
    # Guarda el PDF
    can.save()


def fecha():
    # Obtiene la fecha del sistema
    return str(datetime.today().strftime('%Y-%m-%d'))


def cuentaCaracteres():
    suma = 0
    # Extrae la conversación del fichero
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    # Recorre las líneas del fichero sumando sus caracteres
    for linea in lista_texto:
        suma += len(linea.replace(" ", "").replace(">", "").replace("\n", "").replace("\t", ""))
    return suma


def cuentaPalabras():
    suma = 0
    # Extrae la conversacón del fichero
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    # Recorre la conversación contando las palabras
    for linea in lista_texto:
        suma += len(linea.split())
    return suma


def cuentaDe():
    suma = 0
    # Extrae la conversación del fichero
    with open('conversacion.txt', 'r') as f:
        lista_texto = f.readlines()
    # Recorre la conversación contando las veces que aparece 'de'
    for linea in lista_texto:
        palabras = linea.replace(".", "").replace(",", "").replace(">", "").split()
        for palabra in palabras:
            if palabra == 'de':
                suma += 1
    return suma


# Aplicación principal
print('\t\t\t\t\t\t  \033[1m\033[4mAPLICACIÓN BOT-ARATE\033[0m')

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
