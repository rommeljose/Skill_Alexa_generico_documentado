# -*- coding: utf-8 -*-

# Este ejemplo muestra muestra el manejo de las solicitudes (intents) de una habilidad de Alexa 
# usando el kit de habilidades de Alexa SDK para Python. Visite https://alexa.design/cookbook 
# para ver ejemplos adicionales sobre la implementación de ranuras (slot), administración de diálogos, 
# persistencia de sesiones, llamadas de API y más. Esta muestra se crea utilizando el enfoque de clases de controlador en el generador de habilidades.

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# La Clase "AbstractRequestHandler" es una de las (dos) formas de dministradores las solicitudes a Alexa;
# son responsable de los tipos de solicitudes entrantes de Alexa (la otra es el decorador Skill Builde). 
# Se muestra como configurar un controlador para que se invoque cuando la habilidad recibe un LaunchRequest.
# La clase AbstractRequestHandler, debera implementar los metodos: "can_handle" y "handle".
# Chando el SDK llama un metodo, se invoca el controlador de solicitudes.

# El evento "LaunchRequestHandler" ocurre cuando la habilidad se invoca sin una intención específica.

class LaunchRequestHandler(AbstractRequestHandler):
    """Controlador para el lanzamiento de habilidades."""
    # El metodo canHandle devuelve verdadero si la solicitud entrante es una "LaunchRequest".
    # El metodo para determinar si el controlador dado es capaz de procesar la solicitud entrante. 
    # Esta función acepta un objeto "Handler Input" y espera que se devuelva un booleano. 
    # Si el método devuelve True , se supone que el controlador debe manejar la solicitud con éxito. 
    # Si devuelve False , se supone que el controlador no debe manejar la solicitud de entrada;
    #  por lo tanto, no se ejecuta hasta su finalización.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    # Este metodo o función contiene, la lógica de procesamiento de solicitudes del controlador, 
    # Acepta la entrada del controlador y devuelve un objeto "Response".
    # En el ejemplo, el metodo genera y devuelve una respuesta de saludo básica con objetos
    # de respuestas, como: Speech, Card y Reprompt (ejemplo: una respuesta básica de "Hola ... ").
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hola, ¡eres nuevo con Alexa!"

        return (
            handler_input.response_builder
                .speak(speak_output) 
                #.ask(speak_output)
                .response
        )

# El evento del usuario "HelloWorldIntent", se invoca con la intension manifestada por
# las palabras (ejemp.): "Di hola", "Di hola mundo", "Di tu palabra", "Como estas", etc.
# La funcion "can_handle" detecta si la solicitud entrante es una "IntentRequesty",
# devuelve verdadero si el nombre de la intención es "HelloWorldIntent". 
# La handlefunción genera y devuelve una respuesta básica (ejemplo: "¡Hola mundo!").

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Controlador de solicitudes (Intent), para Hello World."""
    # El metodo canHandle devuelve verdadero si la solicitud entrante es una LaunchRequest. 
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DituPalabraIntent")(handler_input)

    # El metodo genera y devuelve una respuesta de saludo básica con objetos de respuesta 
    # como Speech, Card y Reprompt: genera y se devuelve una respuesta básica de "Hola mundo!".
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "¡Hola mundo !"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("¿que pasa?")
                .response
        )

# Muestra como se configurar el controlador para que se invoque cuando la habilidad recibe la intención
# requerida e incorporada AMAZON.HelpIntent.

class HelpIntentHandler(AbstractRequestHandler):
    """Controlador para la intención de ayuda."""
    # Este controlador (IntentRequest) busca coincidencia con el nombre de intención esperado. 
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    # Se devuelven las instrucciones de ayudas básicas.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Tu unicamente puedes decir -hola hola-, ¿Cómo puedo Ayudarte?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Este controlador ("CancelOrStopIntent"), también se activara mediante las intenciones integradas. 
# En este caso, se usa un solo controlador para responder a dos intentos diferentes:
# "Amazon.CancelIntent" y "Amazon.StopIntent".

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Controlador único para cancelar y detener la intención."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) 

    # La respuesta, será la misma para ambos requerimientos.
    # Tener un solo controlador para dos o más intentos, reduce el código repetitivo.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Adios, que estes bien!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

# A pesar de no poder (ni tener) que enviar una respuesta después de recibir un "SessionEndedRequest", 
# este controlador brinda un lugar para poner la logica de limpieza.
class SessionEndedRequestHandler(AbstractRequestHandler):
    """Controlador para el final de la sesión."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "El Rey Arturo dueño de excalibur!"
        # Cualquier logica de limpieza va aqui..

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """El reflector de intención se utiliza para la prueba y depuracion de modelos de interaccion. Simplemente repetira la intencion que dijo el usuario. Puede crear controladores personalizados para sus intenciones definiéndolos arriba y luego agregandolos a la cadena de controladores de solicitudes a continuacion.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Tu justamente dijistes " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

# A veces, las cosas salen mal y su código de habilidad necesita una forma de manejar el problema con
# elegancia. ASK SDK para Python admite el manejo de excepciones de manera similar al manejo de solicitudes.
# Controladores de excepciones: captura de todas las excepciones a su habilidad,
# garantizar que la habilidad devuelva un mensaje significativo para todas las excepciones.

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Manejo de errores genericos para capturar cualquier error de sintaxis o enrutamiento. Si recibe un error que indica que no se encuentra la cadena del controlador de solicitudes, no ha implementado un controlador para la intencion que se esta invocando ni lo ha incluido en el generador de habilidades a continuacion.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


# El objeto generador de habilidades ("SkillBuider") ayuda a agregar los componentes 
# responsables de manejar las solicitudes de entrada y generar respuestas personalizadas.
# 
# El objeto SkillBuilder actua como punto de entrada para su habilidad, enrutando todas 
# las cargas utiles de solicitud y respuesta a los controladores anteriores. 
# Los controladores o interceptores definidos, deben de estar incluidos a continuacion. 
# El orden importa: se procesan extrictamente de arriba a abajo.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()