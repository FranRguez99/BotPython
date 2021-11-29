import re, os, pickle, random



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


def botsimpleregex():
    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        comprobarentrada(entrada)

botsimpleregex()






