from gtts import gTTS
import speech_recognition as sr
from copying import copy
#from pygame import mixer
from playsound import playsound
import random
from randomwall import randomwallchange
from launch import launcher
import time

# Voice for Edith
def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        #mixer.init()
        playsound('audio.mp3')
        #mixer.music.load("audio.mp3")
        #mixer.music.play()

# Function for listening commands
def listenCmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nova is ready...Speak now!")
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        print("Adjusting for background noise. One second")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something...")
        #listens for the user's input
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            #command = r.recognize_sphinx(audio) #offline_Speech_Recognition
            print("You Said: " + command + "\n")
        #loopback to continue listening for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            print("Your last command couldn\'t be heard.")
            command = listenCmd()
        return command

def edith(command):
    errors = [
        "I can\'t get you!",
        "Can you repeat it please?",
        ]
    wall = ["Hey, I've changed the wallpaper for you. Hope it looks good on your desktop.",
            "Woah, that look awesome on your desktop.",
            "How about this Dude?",
            "Yeah, I've got this Brother! Changed the wall for you."
        ]

    if 'wallpaper' in command or 'wall' in command or 'background' in command:
        randomwallchange()
        response = random.choice(wall)
        talk(response)

    elif 'hello' in command or 'hi' in command or 'hey' in command:
        talk("Hello Diwi! Nova is here to serve you?")

    elif 'launch' in command:
        launcher(command)
        talk("Application launched successfully...")

    elif 'copy' in command:
        copy(command)

    elif 'sleep' in command or 'bye' in command or 'will see you' in command or 'bubye' in command:
        talk("Goodbye Friend. Nova is about to shutdown in 5 seconds, five, four, three, two, one. . .")
        #time.sleep(5)
        exit()

    else:
        response = random.choice(errors)
        talk(response)

talk("Hey. Nova is ready to serve you!")

while True:
    edith(listenCmd())
