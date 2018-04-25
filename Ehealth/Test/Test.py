'''
Created on 25 de abr de 2018

@author: lucas
'''
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx

r = sr.Recognizer()
m = sr.Microphone()







def tell_this_in(tell,lang):
    tts = gTTS(text=tell, lang=lang)
    tts.save("1.mp3")
    os.system("mpg321 /home/lucas/workspace/E-health/Test/1.mp3")


def tell_this_only_english(word_to_tell):
    engine = pyttsx.init()
    engine.say(word_to_tell)
    engine.runAndWait()


try:
    
    #strn = "Silencio por favor. Estou Configurando threshold. Tudo pronto, o que voce deseja mestre?"
    print("Silencio por favor ...")
    #tell_this_in(strn, "pt")
    with m as source: r.adjust_for_ambient_noise(source)
    #print("Configurando threshold para {}".format(r.energy_threshold))
    #tell_this_in("Estou Configurando threshold", "pt")
    #tell_this_in("Tudo pronto. O que voce deseja, mestre?", "pt")
    with m as source: 
        audio = r.listen(source,timeout=3)
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)
        value = "I got it, you said "+value 
        print (value)
        tell_this_only_english(value)
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass