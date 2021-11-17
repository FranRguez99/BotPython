import re , os, pickle
dicrespuestas = {"Hola soy vicente": "Muy buenas, usuario. Soy Botarate",
                 "¿Qué sabes de música?": "Pues la verdad que de eso sé poco",
                 "¿Qué sabes de informática?": "Pues soy un experto, chaval",



                     "Alt": "Pues la verdad de eso poco."}

def botregex():
    inicio = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    while inicio.casefold() != "salir".casefold():
        inicio = input("\t\t>")
        if inicio in dicrespuestas:
            print("\t\t>", dicrespuestas.get(inicio))

        else:
            print("\t\t>", dicrespuestas.get("Alt"))
        print("\t\t\n")





