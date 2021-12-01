# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)
import random


conversacion = False


def inicio(update, context):
    context.bot.send_message(update.message.chat_id, "Oído cocina. Tú dirás...")
    global conversacion
    conversacion = True


def ods(update, context):
    lista_ods = ["Erradicar la pobreza en todas sus formas sigue siendo uno de los principales "
                 "desafíos que enfrenta la humanidad. Si bien la cantidad de personas que viven "
                 "en la extrema pobreza disminuyó en más de la mitad entre 1990 y 2015, aún demasiadas "
                 "luchan por satisfacer las necesidades más básicas.",
                 "Desgraciadamente, el hambre y la desnutrición siguen siendo grandes obstáculos para el "
                 "desarrollo de muchos países. Se estima que 821 millones de personas sufrían de desnutrición "
                 "crónica al 2017, a menudo como consecuencia directa de la degradación ambiental, la sequía y "
                 "la pérdida de biodiversidad. Más de 90 millones de niños menores de cinco años tienen un peso "
                 "peligrosamente bajo. La desnutrición y la inseguridad alimentaria parece estar incrementándose "
                 "tanto en casi todas las de regiones de África, como en América del Sur.",
                 "La buena salud es esencial para el desarrollo sostenible, y la Agenda 2030 refleja la complejidad y "
                 "la interconexión de ambos. Toma en cuenta la ampliación de las desigualdades económicas y sociales, "
                 "la rápida urbanización, las amenazas para el clima y el medio ambiente, la lucha continua contra el "
                 "VIH y otras enfermedades infecciosas, y los nuevos problemas de salud, como las enfermedades no "
                 "transmisibles. La cobertura universal de salud será integral para lograr el ODS 3, terminar con la "
                 "pobreza y reducir las desigualdades. Las prioridades de salud global emergentes que no se incluyen "
                 "explícitamente en los ODS, incluida la resistencia a los antimicrobianos, también demandan acción.",
                 "El objetivo de lograr una educación inclusiva y de calidad para todos se basa en la firme "
                 "convicción de que la educación es uno de los motores más poderosos y probados para garantizar el "
                 "desarrollo sostenible. Con este fin, el objetivo busca asegurar que todas las niñas y niños "
                 "completen su educación primaria y secundaria gratuita para 2030. También aspira a proporcionar "
                 "acceso igualitario a formación técnica asequible y eliminar las disparidades de género e ingresos, "
                 "además de lograr el acceso universal a educación superior de calidad.",
                 "Poner fin a todas las formas de discriminación contra las mujeres y niñas no es solo un derecho "
                 "humano básico, sino que además es crucial para el desarrollo sostenible. Se ha demostrado una y "
                 "otra vez que empoderar a las mujeres y niñas tiene un efecto multiplicador y ayuda a promover el "
                 "crecimiento económico y el desarrollo a nivel mundial.",
                 "Asegurar el agua potable segura y asequible universal implica llegar a más de 800 millones de "
                 "personas que carecen de servicios básicos y mejorar la accesibilidad y seguridad de los servicios "
                 "por más de dos mil millones.",
                 "Entre 2000 y 2016, la cantidad de personas con acceso a energía eléctrica aumentó de 78 a 87 por "
                 "ciento, y el número de personas sin energía bajó a poco menos de mil millones. Sin embargo, "
                 "a la par con el crecimiento de la población mundial, también lo hará la demanda de energía "
                 "accesible, y una economía global dependiente de los combustibles fósiles está generando cambios "
                 "drásticos en nuestro clima.",
                 "Los Objetivos de Desarrollo Sostenible apuntan a estimular el crecimiento económico sostenible "
                 "mediante el aumento de los niveles de productividad y la innovación tecnológica. Fomentar políticas "
                 "que estimulen el espíritu empresarial y la creación de empleo es crucial para este fin, "
                 "así como también las medidas eficaces para erradicar el trabajo forzoso, la esclavitud y el tráfico "
                 "humano. Con estas metas en consideración, el objetivo es lograr empleo pleno y productivo y un "
                 "trabajo decente para todos los hombres y mujeres para 2030.",
                 "Los avances tecnológicos también con esenciales para encontrar soluciones permanentes a los "
                 "desafíos económicos y ambientales, al igual que la oferta de nuevos empleos y la promoción de la "
                 "eficiencia energética. Otras formas importantes para facilitar el desarrollo sostenible son la "
                 "promoción de industrias sostenibles y la inversión en investigación e innovación científicas.",
                 "La desigualad de ingresos es un problema mundial que requiere soluciones globales. Estas incluyen "
                 "mejorar la regulación y el control de los mercados y las instituciones financieras y fomentar la "
                 "asistencia para el desarrollo y la inversión extranjera directa para las regiones que más lo "
                 "necesiten. Otro factor clave para salvar esta distancia es facilitar la migración y la movilidad "
                 "segura de las personas.",
                 "Mejorar la seguridad y la sostenibilidad de las ciudades implica garantizar el acceso a viviendas "
                 "seguras y asequibles y el mejoramiento de los asentamientos marginales. También incluye realizar "
                 "inversiones en transporte público, crear áreas públicas verdes y mejorar la planificación y gestión "
                 "urbana de manera que sea participativa e inclusiva.",
                 "El consumo de una gran proporción de la población mundial sigue siendo insuficiente para satisfacer "
                 "incluso sus necesidades básicas. En este contexto, es importante reducir a la mitad el desperdicio "
                 "per cápita de alimentos en el mundo a nivel de comercio minorista y consumidores para crear cadenas "
                 "de producción y suministro más eficientes. Esto puede aportar a la seguridad alimentaria y "
                 "llevarnos hacia una economía que utilice los recursos de manera más eficiente.",
                 "Las pérdidas anuales promedio causadas solo por catástrofes relacionadas al clima alcanzan los "
                 "cientos de miles de millones de dólares, sin mencionar el impacto humano de las catástrofes "
                 "geofísicas, el 91 por ciento de las cuales son relacionadas al clima, y que entre 1998 y 2017 "
                 "tomaron la vida de 1,3 millones de personas, y dejaron a 4.400 millones heridas. El objetivo busca "
                 "movilizar US$ 100.000 millones anualmente hasta 2020, con el fin de abordar las necesidades de los "
                 "países en desarrollo en cuanto a adaptación al cambio climático e inversión en el desarrollo bajo "
                 "en carbono. "
                 "Los océanos también absorben alrededor del 30% del dióxido de carbón generado por las actividades "
                 "humanas y se ha registrado un 26% de aumento en la acidificación de los mares desde el inicio de la "
                 "revolución industrial. La contaminación marina, que proviene en su mayor parte de fuentes "
                 "terrestres, ha llegado a niveles alarmantes: por cada kilómetro cuadrado de océano hay un promedio "
                 "de 13.000 trozos de desechos plásticos.",
                 "La vida humana depende de la tierra tanto como del océano para su sustento y subsistencia. La flora "
                 "provee el 80% de la alimentación humana y la agricultura representa un recurso económico y un medio "
                 "de desarrollo importante. A su vez, los bosques cubren el 30% de la superficie terrestre, "
                 "proveen hábitats cruciales a millones de especies y son fuente importante de aire limpio y agua. "
                 "Además, son fundamentales para combatir el cambio climático.",
                 "Los Objetivos de Desarrollo Sostenible buscan reducir sustancialmente todas las formas de violencia "
                 "y trabajan con los gobiernos y las comunidades para encontrar soluciones duraderas a los conflictos "
                 "e inseguridad. El fortalecimiento del Estado de derecho y la promoción de los derechos humanos es "
                 "fundamental en este proceso, así como la reducción del flujo de armas ilícitas y la consolidación "
                 "de la participación de los países en desarrollo en las instituciones de gobernabilidad mundial.",
                 "Los Objetivos de Desarrollo Sostenible solo se pueden lograr con el compromiso decidido a favor de "
                 "alianzas mundiales y cooperación. La Asistencia Oficial para el Desarrollo se mantuvo estable pero "
                 "por debajo del objetivo, a US$147.000 millones en 2017, mientras que las crisis humanitarias "
                 "provocadas por conflictos o desastres naturales continúan demandando más recursos y ayuda "
                 "financiera. Muchos países también requieren de esta asistencia para estimular el crecimiento y el "
                 "intercambio comercial."]
    num_ods = random.randint(1, 17)
    global conversacion
    if conversacion == True:
        context.bot.send_message(update.message.chat_id, lista_ods[num_ods])


def cita(update, context):
    lista_citas = ["Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)",
                   "Con demasiada frecuencia damos a los estudiantes respuestas para recordar en lugar de problemas "
                   "para resolver (Roger Lewin)",
                   "Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso "
                   "de introducirlos. (Edsger Dijkstra)",
                   "Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas "
                   "personas que lo practiquen. (Henry Ford)",
                   "No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert "
                   "Einstein)",
                   "Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)",
                   "No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)",
                   "La experiencia demuestra que el éxito de un curso de programación depende críticamente de la "
                   "elección de los ejemplos que se utilice. (Niklaus Wirth)",
                   "Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un "
                   "proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste en "
                   "dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)",
                   "Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)",
                   "Los malos programadores se preocupan del código. Los buenos se preocupan de las estructuras de "
                   "datos y de sus relaciones. (Linus Torvalds)",
                   "La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)",
                   "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)",
                   "El futuro no es lo que va a pasar sino lo que vamos a hacer. (Anónimo)",]
    num_citas = random.randint(1, len(lista_citas))
    global conversacion
    if conversacion == True:
        context.bot.send_message(update.message.chat_id, lista_citas[num_citas])


def final(update, context):
    global conversacion
    if conversacion == True:
        context.bot.send_message(update.message.chat_id, "¡Que pases un buen día amigo!")
        conversacion = False


def main():
    TOKEN = "2115182993:AAEIKig-Dxtn5FT1yH7bTLGVMNV8fxZckK4"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('inicio', inicio))
    dp.add_handler(CommandHandler('ods', ods))
    dp.add_handler(CommandHandler('cita', cita))
    dp.add_handler(CommandHandler('final', final))
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()


if __name__ == '__main__':
    main()