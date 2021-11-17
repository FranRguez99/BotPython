import re, os, pickle, random



def cadpatr(delpatron, delacadena):
    listagrup = re.findall(delpatron, delacadena)
    for palabra in listagrup[0]:
        delacadena = delacadena.replace(palabra, "")
    return delacadena



def comprobarentrada(cadena):
    patroninicio = re.compile(r"^(Hola)(,?)( *soy )", re.IGNORECASE)

    if re.search(patroninicio, cadena):
        nombre = cadpatr(patroninicio, cadena)
        print(f"\t\tMuy buenas, {nombre}. Soy Botarate")


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







