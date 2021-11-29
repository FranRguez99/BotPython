import json, re


def EscribirRespuesta(respuesta,registro):
    guardarEnRegistro(respuesta,registro)
    print(respuesta)


def guardarEnRegistro(texto,registro):
    registro.write(texto)




def cadpatr(delpatron, delacadena):
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena




def Main():
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
                guardarEnRegistro(datosUsuario,registro)
                if datosUsuario == opcionSalir:
                    salir = True
                else:
                    for valores in listaValores:
                        regex = re.compile(valores[0], re.IGNORECASE)
                        if re.search(regex, datosUsuario):
                            variable = cadpatr(regex, datosUsuario)
                            respuesta = valores[1].replace("{variable}", variable).replace("?", "")
                            conoceValor = True
                            EscribirRespuesta(respuesta,registro)
                            break
                    if conoceValor ==  False:
                        EscribirRespuesta(noSabeRespuesta,registro)

            guardarEnRegistro("#### Conversacion terminada ####",registro)

Main()
