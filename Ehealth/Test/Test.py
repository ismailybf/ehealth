# encoding: utf-8
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




def msg_nao_entendi():
    os.system("mpg321 nao_entendi.mp3")
    

def msg_conf():
    os.system("mpg321 silencio.mp3")

def conf():
    os.system("mpg321 conf.mp3")

def get_intro():
    os.system("mpg321 intro.mp3")


def get_info_meningite():
    os.system("mpg321 meningite.mp3")

def yes_or_no():
    os.system("mpg321 yes_or_no.mp3")

def get_pergunta_yes_or_no():
    while True:
        try:
            print "Fale pausadamente"
            yes_or_no()
            audio = r.listen(source,timeout=2)
            try:
                print "Traduzindo para texto..."
                value = r.recognize_google(audio)
                print "Voce disse "+value
                if value == 'yes':
                    return True
                elif value == 'no': 
                    return False
                else: msg_nao_entendi()
            except sr.UnknownValueError:
                print("Desculpe, nao entendi")
                msg_nao_entendi()
            except sr.RequestError:
                print("Desculpe, nao entendi")
                msg_nao_entendi()
        except KeyboardInterrupt:
            pass
    

def get_voice():
    try:
        with m as source: audio = r.listen(source,timeout=3)
        try:
            print "Fale pausadamente"
            value = r.recognize_google(audio)
            print "Voce disse "+value
            return value
        except sr.UnknownValueError:
            print("Nao entendi")
            msg_nao_entendi()
        except sr.RequestError:
            msg_nao_entendi()
            print("Nao entendi")
    except KeyboardInterrupt:
        msg_nao_entendi()    



def tell_this(tell,lang="pt"):
    tts = gTTS(text=tell, lang=lang)
    tts.save("yes_or_no.mp3")
    os.system("mpg321 yes_or_no.mp3")


def tell_this_file(tell,file_use,lang="pt"):
    tts = gTTS(text=tell, lang=lang)
    tts.save(file_use+".mp3")
    os.system("mpg321 "+file_use+".mp3")


def tell_this_only_english(word_to_tell):
    engine = pyttsx.init()
    engine.say(word_to_tell)
    engine.runAndWait()



msg_conf()
with m as source: r.adjust_for_ambient_noise(source)
conf()
get_intro()
with m as source: 
    while True:
        try:
            print "Fale pausadamente"
            yes_or_no()
            audio = r.listen(source,timeout=2)
            try:
                print "Traduzindo para texto..."
                value = r.recognize_google(audio)
                print "Voce disse "+value
                if value == 'yes':
                    get_info_meningite()
                    break
                elif value == 'no': break
                else: msg_nao_entendi()
            except sr.UnknownValueError:
                print("Desculpe, nao entendi")
                msg_nao_entendi()
            except sr.RequestError as e:
                print("Desculpe, nao entendi")
                msg_nao_entendi()
        except KeyboardInterrupt:
            pass

    s = ("Vou fazer algumas perguntas, sobre sua condisao geral. Baseado num artigo"+
        " do hospotal Albert Einsten")
    tell_this_file(s, "pergunta_0")
    s = "Voce sente dores locais nas costas, nos musculos ou pescoso?"
    tell_this_file(s, "pergunta_1")
    #r_1 = get_pergunta_yes_or_no()
    s = ("Voce ocasionalmente sente calafrios, fadiga, febre, letargia, mal-estar,"+
     "perda de apetite ou tremores no corpo?")
    tell_this_file(s, "pergunta_2")
    #r_2 = get_pergunta_yes_or_no()

    s = ("Sobre seu aparelho gastrointestinal, voce sente nahusea ou vmito")
    tell_this_file(s, "pergunta_3")
    #r_3 = get_pergunta_yes_or_no()
    
    
    s = ("Com relasao a sua pele... Ela apresenta erupses, um pouco avermelhadas ou"+ 
    " manchas vermelhas espalh")
    tell_this_file(s, "pergunta_4")
    #r_4 = get_pergunta_yes_or_no()
    #print r_1    
    






'''
    
try:
    
    #strn = "Inflamação das membranas que revestem o cérebro e a medula espinhal, geralmente causada por uma infecção."
    
    
    
    
    #tell_this(strn)
    print("")
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
        value = "Entendi, voce disse "+value 
        print (value)
      #  tell_this(value)
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
'''