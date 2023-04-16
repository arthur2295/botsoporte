# -*- coding: utf-8 -*-
"""botfun.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Kl4B7kFfqadU5lCx-Pq6HY0r6Ozsbp_
"""

!pip install chatterbot2
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Crea una instancia del ChatBot
bot = ChatBot('Support Bot')

# Agrega preguntas y respuestas al bot
conversation = [
    'Hola',
    '¡Hola! ¿En qué puedo ayudarte?',
    '¿Cómo restablezco mi contraseña?',
    'Para restablecer tu contraseña, ve a la página de inicio de sesión y haz clic en "¿Olvidaste tu contraseña?"',
    '¿Cómo puedo entrar a steam virtual?',
    'para entrar a steam virtual, primero asegúrate de que estes entrando con el correo que te registrarte. Luego, sigue las instrucciones proporcionadas por steam virtual.'
]

trainer = ListTrainer(bot)
trainer.train(conversation)

# Define una función para procesar las solicitudes de los estudiantes
def get_response(message):
    # Genera una respuesta del bot a partir del mensaje del estudiante
    response = bot.get_response(message)

    # personalizar la respuesta del bot en función de las necesidades de soporte técnico
    if 'steam virtual' in message:
        print('Bot: puedes observar este pdf para guiarte, aqui encontrarasuna guia para entrar a steam virtual ')
        response = "https://drive.google..............."      
    elif 'plataforma' in message:
        response = '¿Podrías proporcionar más detalles sobre el problema que estás experimentando?'
    if 'soporte tecnico' in message:
        print('puedes guiarte con el soporte tecnico aqui:')
        response = 'mmmmmmm'

    return str(response)

# Define una función para iniciar una conversación con el bot
def start_conversation():
    print('¡Bienvenido al bot de soporte técnico para estudiantes! Por favor ingrese su pregunta o problema técnico:')
    while True:
        message = input('Yo: ')
        if message.lower() == 'adios':
            print('Bot: ¡Hasta luego!')
            break
        else:
            response = get_response(message)
            print('Bot:', response)

# Inicia la conversación con el bot
start_conversation()
