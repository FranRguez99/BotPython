import re
import random
#aquí se evitan signos de puntuación
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
#aquí se calcula la probabilidad del mensaje
def message_probability(user_message, recognized_words, respuesta_simple=False, required_word=[]):
    message_certainty = 0
    has_required_words = True
#aquí se hace un reconocimiento del mensaje de usuario
    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or respuesta_simple:
        return int(percentage * 100)
    else:
        return 0
#aquí se checa de todos los mensajes la mayor probabilidad
def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words,respuesta_simple = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, respuesta_simple, required_words)
        #aquí se crean las respuestas a las preguntas
        response('Hola Alex', ['Hola', 'saludos', 'buenas'], respuesta_simple = True)
        response('Estoy bien y tu?', ['cómo', 'estas', 'va', 'vas', 'sientes',"que sientes"], required_words=['como'])
        response('De animales nosé nada', ['bichos', 'animales', 'mundo_animal',], required_words=['animales'])
        response('Suspendí la asignatura de ciberseguridad en la universidad', ['seguridad', 'ciberseguridad',],required_words=['ciberseguridad'])
        response('Hablemos de videojuegos yo los amo', ['videojuegos', 'Videojuegos?',"que","sabes"],required_words=['videojuegos'])
        response('Estamos en la calle calatrava', ['estoy', 'direccion', 'donde', 'estamos'], respuesta_simple=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], respuesta_simple=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match
#si el mensaje es desconcido se da esta respuesta
def unknown():
    response = ['no entiendo lo que pretendes decirme',][random.randrange(3)]
    return response

while True:
    print("Yurena: " + get_response(input('You:')))