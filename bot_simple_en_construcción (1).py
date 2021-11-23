frases = {
        "¿Qué tal?": "bien",
         "Hola": "Hola",
         "¿qué sabes de animales?":"Mi animal favorito es el orangután",
        "¿qué sabes de videojuegos?":"Me encanta mortal kombat lo juego 24/7",
        "¿qué sabes de Anime?":"El viaje de chihiro es una gran película",
       "¿dónde estamos?":"En la calle calatrava en el SAFA",
        "¿qué haces ahora?":"Ahora mismo estoy respondiendote a ti y me siento bastante bien",
        "¿qué hiciste ayer?":"Ayer repartí el oro del mundo como Robin Hood",
        "Adiós":"Adios"
         }
frase=input("yo:")
#meterlo en un while hasta que se diga adios
while frase !="adios":

 if frase==frases.get(frase):
  print("yurena:"+str(frases()))
else:
 print("yurena:esa oración no tiene respuesta")
