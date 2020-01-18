from gtts import gTTS
from playsound import playsound

def talkvoice(audio):
    print("NOVA: " + audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        playsound('audio.mp3')
    return