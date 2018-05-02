    
# -*- coding: utf-8 -*-#

'''
Created on 25 de abr de 2018

@author: lucas
'''
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx
import webbrowser



def msg_dont_get_it():
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


def tell_this(tell,lang="pt"):
    tts = gTTS(text=tell, lang=lang)
    tts.save("yes_or_no.mp3")
    os.system("mpg321 yes_or_no.mp3")


def tell_this_file(tell,file_use,lang="pt"):
    tts = gTTS(text=tell, lang=lang)
    tts.save(file_use+".mp3")
    os.system("mpg321 "+file_use+".mp3")



def get_open_question():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source: 
        r.adjust_for_ambient_noise(source)
        cont = 0
        while True:
            try:
                print "Fale pausadamente"       
                audio = r.listen(source)
                try:
                    print "Traduzindo para texto..."
                    value = r.recognize_google(audio,language='pt-BR')
                    print "Resposta = "+value
                    return value
                except sr.UnknownValueError:
                    if cont<3:
                        print("Desculpe, não entendi")
                        msg_dont_get_it()
                except sr.RequestError:
                    if cont<3:
                        print("Desculpe, não entendi")
                        msg_dont_get_it()
            except KeyboardInterrupt:
                pass



def get_yes_or_no_question():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source: 
        r.adjust_for_ambient_noise(source)
        cont = 0
        while True:
            if cont>=3:
                s = "Por favor, use o teclado digitando 1 para sim e 2 para nao."
                print "Por favor, use o teclado digitando 1 para sim e 2 para não." 
                tell_this_file(s,"mensagem_teclado_1")
                res = input()
                if res==1: return True
                elif res==2: return False
                else:
                    continue
            try:
                cont+=1
                print "Fale pausadamente"
                
                yes_or_no()
                audio = r.listen(source)
                try:
                    print "Traduzindo para texto..."
                    value = r.recognize_google(audio,language='pt-BR')
                    print "Resposta = "+value
                    if "sim" in value:
                        return True
                    elif "n" in value: 
                        return False
                    else: msg_dont_get_it()
                except sr.UnknownValueError:
                    if cont<3:
                        print("Desculpe, não entendi")
                        msg_dont_get_it()
                except sr.RequestError:
                    if cont<3:
                        print("Desculpe, não entendi")
                        msg_dont_get_it()
            except KeyboardInterrupt:
                pass


def tell_this_only_english(word_to_tell):
    engine = pyttsx.init()
    engine.say(word_to_tell)
    engine.runAndWait()


def menu():    
    print "Diga o que você deseja saber sobre a doença. Eu sei informações como, por exemplo" 
    print " Como a meningite se propaga"
    print " Como é o Tratamento"
    print " Quais os Medicamentos"
    print " Quais Cuidados médicos"
    print " Quais Especialistas procurar"
    print " Ou diga sair para encerrar"
    os.system("mpg321 menu_0.mp3")
    os.system("mpg321 menu_1.mp3")
    os.system("mpg321 menu_2.mp3")
    os.system("mpg321 menu_3.mp3")
    os.system("mpg321 menu_4.mp3")
    os.system("mpg321 menu_5.mp3")
    os.system("mpg321 menu_6.mp3")


if __name__ == '__main__':
        
    msg_conf()
    conf()
    get_intro()
    intro = get_yes_or_no_question()
    if intro == True: get_info_meningite()  
    question_0 = ("Vou fazer algumas perguntas, sobre sua condissao geral. Baseado num artigo"+
        " do hospital Albert Einsten")
    print ("Vou fazer algumas perguntas, sobre sua condição geral. Baseado num artigo \n"+
        " do hospital Albert Einsten")
    tell_this_file(question_0, "question_0")
    
    question_1 = "Voce sente dores locais nas costas, nos musculos ou no pescosso?"
    print ("Você sente dores locais nas costas, nos músculos ou no pescoço?")
    tell_this_file(question_1, "question_1")
    r_1 = get_yes_or_no_question()
    
    question_2 = ("Voce ocasionalmente sente calafrios, fadiga, febre, letargia, mal-estar,"+
     "perda de apetite ou tremores no corpo?")
    
    print ("Você ocasionalmente sente calafrios, fadiga, febre, letargia, mal-estar,\n"+
     "perda de apetite ou tremores no corpo?")
    tell_this_file(question_2, "question_2")
    r_2 = get_yes_or_no_question()

    question_3 = ("Sobre seu aparelho gastrointestinal, voce sente nausea ou vomito?")
    print ("Sobre seu aparelho gastrointestinal, você sente náusea ou vômito?")
    tell_this_file(question_3, "question_3")
    r_3 = get_yes_or_no_question()
    
    
    question_4 = ("Com relassao a sua pele... Ela apresenta erupssoes um pouco avermelhadas ou"+ 
    " manchas vermelhas espalhadas pelo corpo em geral?")
    print ("Com relação a sua pele... Ela apresenta erupções um pouco avermelhadas ou \n"+ 
    " manchas vermelhas espalhadas pelo corpo em geral?")
    tell_this_file(question_4, "question_4")
    r_4 = get_yes_or_no_question()

    
    question_5 = ("Voce esta sentido ou sentiu algum tipo de confusao mental? Como medo de sons altos ou irritabilidade?")
    print ("Você esta sentindo ou sentiu algum tipo de confusão mental? Como medo de sons altos ou irritabilidade?")
    tell_this_file(question_5, "question_5")
    r_5 = get_yes_or_no_question()
    
    question_6 = ("Por fim, voce esta com  a respirassao acelerada, ritmo cardiaco alterado, sensibilidade a luz ou sonolencia?")
    print ("Por fim, você está com a respiração acelerada, ritmo cardíaco alterado, sensibilidade à luz ou sonolência?")
    tell_this_file(question_6, "question_6")
    r_6 = get_yes_or_no_question()
    
    
    answers = ("Aguarde um momento enquanto eu analizo as suas respostas....")
    print ("Aguarde um momento enquanto eu analizo as suas respostas....")
    tell_this_file(answers, "respostas")
    
    
    qdt_yes= r_1+r_2+r_3+r_4+r_1+r_5+r_6
    #qdt_yes=4
    if qdt_yes>=3:
        str_yes = ("Bem... De acordo com o meu modelo, voce pode ter meningite e eu recomendo que procure ajuda e "+
         " realize exames clihnicos. Enquanto isso, voce quer saber mais sobre tratamentos e cuidados?")
        
        print ("Bem... De acordo com o meu modelo, você pode ter meningite e eu recomendo que procure ajuda e \n"+
         " realize exames clínicos. Enquanto isso, você quer saber mais sobre tratamentos e cuidados?")
        tell_this_file(str_yes, "final_yes")
        res = get_yes_or_no_question()
        if res==True:
            while True:
                menu()
                op = get_open_question()
                if "propaga" in op:
                    mens = ("Entendi, voce quer saber sobre como a meningite se propaga.")
                    tell_this_file(mens, "propaga")  
                    mens =("De acordo com os especialistas, ela se propaga por goticulas respiratorias"+
                     "no ar, como por exemplo, tosse ou espirro de pessoas.")
                    tell_this_file(mens, "propaga")
                    question = "Gostaria de continuar?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "tratamento" in op:
                    mens = ("Entendi, voce quer saber mais sobre o tratamento da meningite.")
                    tell_this_file(mens, "tratamento")  
                    mens =("O tratamento varia dependendo da causa, a meningite pode melhorar com o tempo"+
                            " ou pode ser fatal, necessitando de tratamento antibiotico urgente.")
                    tell_this_file(mens, "tratamento")
                    question = "Gostaria de continuar?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "medicamentos" in op:
                    mens = ("Entendi, voce quer saber mais sobre os medicamentos para a meningite.")
                    tell_this_file(mens, "medicamento")  
                    mens =("Os medicamentos sao... antibiotico: mata bacterias ou interrompe o desenvolvimento delas."+
                           " Corticoide: Modifica ou simula efeitos hormonais, muitas vezes para reduzir a inflamassao"+
                            " ou aumentar o crescimento e a reparassao tecidual. Penicilina: Mata bacterias especificas"+ 
                            " ou interrompe o desenvolvimento delas.")
                    tell_this_file(mens, "tratamento")
                    question = "Gostaria de continuar?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if True: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "especialistas" in op:
                    mens = ("Entendi, voce quer saber sobre os especialistas.")
                    tell_this_file(mens, "especia")  
                    mens =("Os especialistas sao...Infectologista que Trata infecssoes, incluindo as de natureza tropical."+
                            "Neurologista: Trata doenssas do sistema nervoso. Pediatra: Fornece assistencia medica para "+
                            ", crianssas e adolescentes. Clinico geral: Previne, diagnostica e trata doensas. "+
                            "Mehdico de emergencia: Trata pacientes no setor de emergencia.")
                    tell_this_file(mens, "tratamento")
                    question = "Gostaria de continuar?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "cuidados" in op:
                    mens = ("Entendi, voce quer saber sobre os cuidados medicos.")
                    tell_this_file(mens, "cuidados")  
                    mens =("Muito repouso, e eventualmente oxigenoterapia que eh o Fornecimento de oxigenio"+
                     " extra para os pulmoes de pessoas com problemas respiratorios.")
                    tell_this_file(mens, "cuidados")
                    question = "Gostaria de continuar?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "sair" in op:
                    mens = ("Obrigado e ateh mais.")
                    print ("Obrigado e até mais.")
                    tell_this_file(mens, "tchau",)    
                    break
                    
                else:
                    question = "Nao entendi....Gostaria de tentar novamente?"
                    tell_this_file(question, "continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: continue
                    else: 
                        mens = ("Obrigado e ateh mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break 
        else:
            mens = ("Obrigado e ateh mais.")
            print ("Obrigado e até mais.")
            tell_this_file(mens, "tchau",)    
        
    else: 
        str_no = ("Bem... Provavelmente voce nao tem meningite. Mas cuide sempre da sua saude, mantenha uma alimentasao"+
    " saudavel e pratique exercicios regularmente. Obrigado e ateh mais.") 
        print ("Bem... Provavelmente você não tem meningite. Mas cuide sempre da sua saude, mantenha uma alimentação\n"+
    " saudável e pratique exercícios regularmente. Obrigado e até mais.") 
        tell_this_file(str_no, "final_no")
        #webbrowser.open_new("https://www.google.com")
        
        
        
     

    
    
    
    






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