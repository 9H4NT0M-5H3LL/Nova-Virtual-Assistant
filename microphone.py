import speech_recognition as sr

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