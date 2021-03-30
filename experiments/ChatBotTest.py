from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
##speech
import pyttsx3
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[0].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()
##speech

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'experiments/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

while True:
    message = input('You:')
    print(message)
    speak(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        speak(reply)
        print('ChatBot:', reply)