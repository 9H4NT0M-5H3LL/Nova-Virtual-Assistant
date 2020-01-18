from microphone import listenCmd
from voiceback import talkvoice
from copying import copy
from csrf import detect_csrf
from playsound import playsound
import random
from randomwall import randomwallchange
from launch import launcher
import time

def edith(command):
    errors = ["I can\'t get you!",
              "Can you repeat it please?",]
    wall = ["Hey, I've changed the wallpaper for you. Hope it looks good on your desktop.",
            "Woah, that look awesome on your desktop.",
            "How about this Dude?",
            "Yeah, I've got this Brother! Changed the wall for you.",]

    if 'wallpaper' in command or 'wall' in command or 'background' in command:
        randomwallchange()
        response = random.choice(wall)
        talkvoice(response)

    elif 'hello' in command or 'hi' in command or 'hey' in command:
        talkvoice("Hello Diwi! Nova is here to serve you?")

    elif 'launch' in command:
        launcher(command)
        talkvoice("Application launched successfully...")

    elif 'cross site request forgery' in command or 'csrf' in command or 'c s r f' in command:
        detect_csrf()

    elif 'copy' in command:
        copy(command)

    elif 'shutup' in command or 'shut your mouth' in command or 'bye' in command or 'will see you' in command or 'bubye' in command:
        talkvoice("Goodbye Friend. Nova is about to shutdown in 5 seconds, five, four, three, two, one. . .")
        exit()

    else:
        response = random.choice(errors)
        talkvoice(response)

talkvoice("Hey. Nova is ready!")
while True:
    edith(listenCmd())
