import json, re


def escribirRespuesta(respuesta, registro):
    guardarEnRegistro(respuesta, registro)
    print(respuesta)


def guardarEnRegistro(texto, registro):
    registro.write(texto)


def cadpatr(delpatron, delacadena):
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
                            variable = cadpatr(regex, datosUsuario)
                            respuesta = valores[1].replace("{variable}", variable).replace("?", "")
                            conoceValor = True
                            escribirRespuesta(respuesta, registro)
                            break
                    if not conoceValor:
                        escribirRespuesta(noSabeRespuesta, registro)

            guardarEnRegistro("#### Conversacion terminada ####", registro)


botRegexFichero()
