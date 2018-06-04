# -*- coding: utf-8 -*-#

'''
Created on 24 de mai de 2018

@author: lucas
'''
    
import googlesearch.googlesearch as gs
import unicodedata
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx
import webbrowser
import requests
from bs4 import BeautifulSoup
import wikipedia as wiki
from nose import result
from PIL import Image
wiki.set_lang("pt")
import time




dir_files="Files/"





def set_file_dir(string):
    dir_files = string
    print dir_files

def get_file_dir():
    print dir_files

def msg_dont_get_it():
    os.system("mpg321 "+dir_files+"nao_entendi.mp3")
    time.sleep(3)

    


def msg_browser():
    print "Deseja informações mais detalhadas no site que encontrei? Eu posso colocar no seu navegador."
    print "Ah, você pode ler com calma e retornar quando quiser, que eu estarei esperando. Quando voltar basta me chamar"
        
    os.system("mpg321 "+dir_files+"abrir_nav_1.mp3")
    os.system("mpg321 "+dir_files+"abrir_nav_2.mp3")
    


def msg_conf():
    mens = "Silêncio por favor, estou configurando o threshold para melhor captar o som"
    print mens
    os.system("mpg321 "+dir_files+"silencio.mp3")

def conf():
    print "Tudo pronto. Threshod configurado para 24000 Hz e 32 kbits/s"
    os.system("mpg321 "+dir_files+"conf.mp3")

def get_intro_meningite():
    mens= "Você disse 'meningite', e vou lhe ajudar no diagnóstico. Mas antes, você quer mais informações sobre a doença?"
    print mens
    get_voice_from_this("intro_meningite")
   

def get_intro():
    mens= "Olá, eu sou Cassandra e estou aqui para lhe ajudar."
    print mens
    os.system("mpg321 "+dir_files+"intro.mp3")


def get_info_meningite():
    mini = ("A meningite é um processo inflamatório das meninges, membranas que envolvem o cérebro e\n"+
    " a medula espinhal. Pode ser causada por diversos agentes infecciosos, como bactérias, vírus,\n"+
    " parasitas e fungos, ou também por processos nao infecciosos. As meningites bacterianas e virais\n"+ 
    " são as mais importantes do ponto de vista da saúde pública, devido sua magnitude, capacidade de\n"+ 
    " ocasionar surtos e no caso da meningite bacteriana a gravidade dos casos.\n"+ 
    " No Brasil, a meningite é considerada uma doença endêmica, deste modo, casos da doença são\n"+
    " esperados ao longo de todo o ano com a ocorrência de surtos e epidemias ocasionais. \n"+
    " A ocorrência das meningites bacterianas é mais comum no inverno e das virais no verão.")

    print mini
    os.system("mpg321 "+dir_files+"meningite_1.mp3")
    os.system("mpg321 "+dir_files+"meningite_2.mp3")
    os.system("mpg321 "+dir_files+"meningite_3.mp3")
        

def yes_or_no():
    os.system("mpg321 "+dir_files+"yes_or_no.mp3")


def tell_this(tell,lang="pt"):
    tts = gTTS(text=unicode(tell,"utf-8"), lang=lang)
    tts.save(dir_files+"1.mp3")
    os.system("mpg321 "+dir_files+"1.mp3")


def tell_this_file(tell,file_use,lang="pt"):
    tts = gTTS(text=unicode(tell,"utf-8"), lang=lang)
    tts.save(dir_files+file_use+".mp3")
    os.system("mpg321 "+dir_files+""+file_use+".mp3")


def get_wikipedia_search(search):
    tell_this("Você deseja a busca: "+search)
    print "Você deseja a busca: "+search
    try:
        results = wiki.search(search,3)
        if not results or results==None or results ==[]:
            tell_this("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
            return False
            
        query = results[0]
        url = wiki.page(query).url
        result_content=wiki.summary(query, sentences=3)
        print "lendo informações em:", 
        print url
        print result_content
        tell_this("Busca concluída, um momento...")
        result_content = unicodedata.normalize('NFKD',result_content).encode('utf-8','ignore')
        tell_this(result_content)
        msg_browser()
        res = get_yes_or_no_question()
        if res:
            webbrowser.open(url)    
            return True
        return False
    except:
        tell_this("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        return False

def get_google_search(search,num_search=3):
    
    tell_this("Você deseja a busca: "+search)
    try:
        response = gs.GoogleSearch().search(search,num_search,"pt-br")
    except:
        print "Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras."
        tell_this("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        return False        

    if not response:
        tell_this("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        print ("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        return False
    results = response.results
    meta_max = ""
    url_max =""
    for res in results:
        url = res.url
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        metas = soup.find_all('meta')
        for meta in metas:
            if 'name' in meta.attrs:
                if meta.attrs['name']=='description':
                    s =  meta.attrs['content']
                    if len(s)>len(meta_max):
                        meta_max = s
                        url_max = url
    if len(meta_max)>0: 
        print "lendo informações em "+url_max
        tell_this("Busca concluída, um momento...")
        print meta_max
        meta_max = unicodedata.normalize('NFKD',meta_max).encode('utf-8','ignore')
        tell_this(meta_max)
        msg_browser()
        res = get_yes_or_no_question()
        if res:
            webbrowser.open(url)    
            return True
        return False
    else:
        tell_this("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        print ("Desculpe, não consegui encontrar sua busca. Tente novamente com outras palavras.")
        return False


def get_search(search):
   
    search = unicodedata.normalize('NFKD',search).encode('utf-8','ignore').lower()
    
    
    
    if ("o que e" in search) or ("quem e" in search):
        return get_wikipedia_search(search)
    return get_google_search(search)
    
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

def waiting_ask():
    r = sr.Recognizer()
    m = sr.Microphone()
    cont=1
    with m as source: 
        r.adjust_for_ambient_noise(source)              
        while True:
            try:
                print "Esperando..."            
                if cont>=1:
                    opt = raw_input("Esperei muito...Desse modo, meu microfone perdeu qualidade, me chame por aqui.")
                    if "Cassandra" in opt:
                        tell_this("Olá, ainda estou aqui.")
                        return True         
                audio = r.listen(source,1)
                cont +=1
                
                try:
                    value = r.recognize_google(audio,language='pt-BR')
                    print "Resposta = "+value
                    if "Cassandra" in value or "Kassandra" in value:
                        tell_this("Olá, ainda estou aqui.")
                        return True
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    pass
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
                s = "Por favor, use o teclado digitando 1 para sim e 2 para não."
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
                    else:
                        msg_dont_get_it()

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

def get_voice_from_this(question):
    os.system("mpg321 "+dir_files+question+".mp3")



def short_general_menu():    
    tell= "Diga o que você deseja saber." 
    print tell 
    get_voice_from_this("short_general_menu")
    

def general_menu():    
    tell= "Diga o que você deseja saber. Eu sei informações sobre a meningite, mas também consigo efetuar buscas no google e a wikipédia"
    tell_2= "Você pode dizer, por exemplo, 'meningite', e eu posso lhe ajudar no diagnóstico. Ou você pode fazer alguma pergunta, como por exemplo, o que é um antibiótico?"
    tell_3 = ("Também posso simular um caso real para testar seus conhecimentos")
    print tell
    print tell_2
    print tell_3
    # tell_this_file(tell_3, "general_menu_3")
    get_voice_from_this("general_menu_1")
    get_voice_from_this("general_menu_2")
    get_voice_from_this("general_menu_3")
    
    
def menu():    
    print "Diga o que você deseja saber sobre a doença. Eu sei informações como, por exemplo:" 
    print " Como a meningite se propaga?"
    print " Como é o Tratamento?"
    print " Quais os Medicamentos?"
    print " Quais Cuidados médicos?"
    print " Quais Especialistas procurar?"
    print " Ou diga sair para encerrar?"
    get_voice_from_this("menu_0")
    get_voice_from_this("menu_1")
    get_voice_from_this("menu_2")
    get_voice_from_this("menu_3")
    get_voice_from_this("menu_4")
    get_voice_from_this("menu_5")
    get_voice_from_this("menu_6")
    
def menu_2():
    print "Diga o que você deseja saber sobre a doença"  
    get_voice_from_this("menu_resumido")
      
def get_meningite(): 
    get_intro_meningite()
    intro = get_yes_or_no_question()
    if intro == True: get_info_meningite()  
    print ("Vou fazer algumas perguntas sobre sua condição geral baseado num artigo \n"+
        " do hospital Albert Einsten")
    get_voice_from_this("question_0")

    print ("Você sente dores locais nas costas, nos músculos ou no pescoço?")
    get_voice_from_this("question_1")
    r_1 = get_yes_or_no_question()
    
    print ("Você ocasionalmente sente calafrios, fadiga, febre, letargia, mal-estar,\n"+
     "perda de apetite ou tremores no corpo?")
    get_voice_from_this("question_2")
    r_2 = get_yes_or_no_question()

    print ("Sobre seu aparelho gastrointestinal, você sente náusea ou vômito?")
    get_voice_from_this("question_3")
    r_3 = get_yes_or_no_question()
    
    
    print ("Com diz respeito a sua pele... Ela apresenta erupções um pouco avermelhadas ou \n"+ 
    " manchas vermelhas espalhadas pelo corpo?")
    get_voice_from_this("question_4")
    r_4 = get_yes_or_no_question()

    
    print ("Você esta sentindo ou sentiu algum tipo de confusão mental? Como, por exemplo, medo"+ 
    "de sons altos ou irritabilidade?")
    get_voice_from_this("question_5")
    get_voice_from_this("question_5_1")
    r_5 = get_yes_or_no_question()
    
    
    print ("E finalmente, você está com a respiração acelerada, ritmo cardíaco alterado ou sensibilidade a luz?")
    get_voice_from_this("question_6")
    r_6 = get_yes_or_no_question()
    
    
    answers = ("Aguarde um momento enquanto eu processo as suas respostas....")
    print ("Aguarde um momento enquanto eu processo as suas respostas....")
    tell_this_file(answers, "respostas")
    qdt_yes= r_1+r_2+r_3+r_4+r_1+r_5+r_6
    if qdt_yes>=3: 
        print ("Bem... De acordo com o meu modelo, você pode ter meningite e eu recomendo que procure ajuda e \n"+
         " realize exames clínicos. Enquanto isso, você quer saber mais sobre tratamentos e cuidados?")
        get_voice_from_this("final_yes")
        res = get_yes_or_no_question()
        menu_resumido=False
        if res==True:
            while True:
                if menu_resumido: menu_2()
                else: menu()
                op = get_open_question()
                if "propaga" in op:
                    print ("Entendi, você quer saber sobre como a meningite se propaga.")  
                    get_voice_from_this("propaga_ask")
                    print ("De acordo com os especialistas, ela se propaga por gotículas respiratórias\n"+
                     "no ar, como por exemplo, tosse ou espirro de pessoas.")
                    get_voice_from_this("propaga_anwser")
                    print "Gostaria de continuar?"
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res:
                        menu_resumido=True 
                        continue
                       
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "tratamento" in op:
                    print ("Entendi, você quer saber mais sobre o tratamento da meningite.")
                    get_voice_from_this("tratamento_ask")
                    print ("O tratamento varia dependendo da causa, a meningite pode melhorar com o tempo"+
                            " ou pode ser fatal, necessitando de tratamento antibiótico urgente.")
                    get_voice_from_this("tratamento_answer")
                    print "Gostaria de continuar?"
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res: 
                        menu_resumido=True
                        continue
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "medicamentos" in op:
                    print ("Entendi, você quer saber mais sobre os medicamentos para a meningite.")
                    get_voice_from_this("medicamento_ask")  
                    print ("Os medicamentos são... antibiótico: mata bactérias ou interrompe o desenvolvimento delas.\n"+
                           " Corticóide: Modifica ou simula efeitos hormonais, muitas vezes para reduzir a inflamação\n"+
                            " ou aumentar o crescimento e a reparação tecidual. Penicilina: Mata bactérias específicas\n"+ 
                            " ou interrompe o desenvolvimento delas.")
                    get_voice_from_this("medicamento_answer_1")
                    get_voice_from_this("medicamento_answer_2_1")
                    get_voice_from_this("medicamento_answer_2_2")
                    get_voice_from_this("medicamento_answer_3")
                    print "Gostaria de continuar?"
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res:
                        menu_resumido = True 
                        continue
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "especialistas" in op:
                    print ("Entendi, você quer saber sobre os especialistas.") 
                    get_voice_from_this("especialistas_ask")
                    get_voice_from_this("especialistas_answer_1")
                    get_voice_from_this("especialistas_answer_2")
                    get_voice_from_this("especialistas_answer_3")
                    get_voice_from_this("especialistas_answer_4")
                    get_voice_from_this("especialistas_answer_5")
                    print "Gostaria de continuar?"
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res:
                        menu_resumido = True 
                        continue
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "cuidados" in op:
                    print ("Entendi, você quer saber sobre os cuidados médicos.")  
                    get_voice_from_this("cuidados_ask")
                    print ("Muito repouso, e eventualmente oxigenoterapia que é o Fornecimento de oxigênio \n"+
                     " extra para os pulmões de pessoas que tem problemas respiratórios.")
                    get_voice_from_this("cuidados_answer_1")
                    get_voice_from_this("cuidados_answer_2")
                    print "Gostaria de continuar?"
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res:
                        menu_resumido = True 
                        continue
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break
                elif "sair" in op:
                    mens = ("Obrigado e até mais.")
                    print ("Obrigado e até mais.")
                    tell_this_file(mens, "tchau",)    
                    break
                    
                else:
                    result = get_search(op)
                    if result: waiting_ask()
                    get_voice_from_this("continuar_ou_sair")
                    res = get_yes_or_no_question()
                    if res:
                        menu_resumido = True 
                        continue
                    else: 
                        mens = ("Obrigado e até mais.")
                        print ("Obrigado e até mais.")
                        tell_this_file(mens, "tchau",)    
                        break 
        else:
            mens = ("Obrigado e até mais.")
            print ("Obrigado e até mais.")
            tell_this_file(mens, "tchau",)    
        
    else: 
        print ("Ok... Provavelmente você não tem meningite. Mas cuide sempre da sua saude, mantenha uma alimentação\n"+
    " saudável e pratique exercícios regularmente. Obrigado e até mais.") 
        get_voice_from_this("final_no_1")
        get_voice_from_this("final_no_2")
        get_voice_from_this("final_no_3")
        #webbrowser.open_new("https://www.google.com")


def resp_diagnostico():
    print "Primeiro irei lhe fazer algumas perguntas antes de perguntar o diagnóstico."
    get_voice_from_this("diag_intro")
    resp_correct1 = set(["lesão púrpura", "taquicardia","hipotensão", "dor no pescoço", "pt e ppt prolongado",
                        "creatina elevada", "cálcio baixo", "mangnésio baixo", "fósforo baixo"])
    resp_correct2 = set(["meningite bactériana", "meningite viral", "encefalite", "tromboflebite infecciosa",
                         "abcesso cerebral", "empiema subdural"])


    get_voice_from_this("diag_q1")
    while True:
        print "Quais foram os sintomas principais apresentados pelo paciente?"
        resp = get_open_question()
        resp_set = set(resp.split())
        if len(resp_set & resp_correct1) > 1 & len(resp_set - resp_correct1) == 0:
            print "Você acertou!"
            t = "Você acertou!"
            tell_this(t)
            tell_this_file(resp)
            dif = list(resp_correct1 - resp_set)
            dif_s = ", ".join(dif)
            s = "Também são respostas: "
            s = s+dif_s
            tell_this(s)
            break
        elif len(resp_set & resp_correct1) > 1:
            m = "Tente fornecer mais de um sintoma"
            print m
            tell_this(m)
        elif len(resp_set - resp_correct1) == 0:
            dif = list(resp_set - resp_correct1)
            dif_s = ", ".join(dif)
            s ="O seguintes sintomas na sua resposta não são corretos: "
            s = s + dif_s
            print s
            tell_this(s)
        else:
            print("Desculpe, não entendi")
            msg_dont_get_it()
            time.sleep(1.0)

    get_voice_from_this("diag_q2")
    while True:
        print "Quais são os possíveis diagnósticos para esse caso?"
        resp = get_open_question()
        resp_set = set(resp.split())
        if len(resp_set & resp_correct2) > 1 & len(resp_set - resp_correct2) == 0:
            print "Você acertou!"
            t = "Você acertou!"
            tell_this(t)
            tell_this_file(resp)
            dif = list(resp_correct2 - resp_set)
            dif_s = ", ".join(dif)
            s = "Também são respostas: "
            s = s + dif_s
            tell_this(s)
            break
        elif len(resp_set & resp_correct2) > 1:
            m = "Tente fornecer mais de um sintoma"
            tell_this(m)
        elif len(resp_set - resp_correct2) == 0:
            dif = list(resp_set - resp_correct2)
            dif_s = ", ".join(dif)
            s = "O seguintes diagnósticos na sua resposta não são corretos: "
            s = s + dif_s
            tell_this(s)
        else:
            print("Desculpe, não entendi")
            msg_dont_get_it()
            time.sleep(1.0)


    get_voice_from_this("diag_q3")
    while True:
        print "Qual é o diagnóstico mais provável?"
        resp = get_open_question()
        if "sair" in resp:
            break
        elif "meningite bactériana" in resp:
            m = "Você acertou! Parabéns!"
            print m
            tell_this(m)
        else:
            m = "Você não acertou tente novamente ou diga sair para desistir"
            print m
            tell_this(m)


def resp_hist_doenca():
    print "O paciente reportou que teve dor de garganta na semana passada. Além disso, um dia antes de vir ao hospital," \
          " o paciente teve vomito e náuse. No dia que veio ao hospital o paciente começou a sentir fadiga, dor de cabeça," \
          "dor no pescoço e fotofobia."
    get_voice_from_this("resp_hp")

def resp_hist_medico():
    print "O paciente não tem histórico de dor abnominal, mordida de carrapato, doença sexualmente transmissível ou " \
          "viagem recente. O paciente também recebeu vacina contra meningite seis meses antes de entrar no hospital."
    get_voice_from_this("resp_hm")

def resp_hist_familiar():
    print "Histórico não disponível"
    get_voice_from_this("resp_hf")

def resp_exam_fisico():
    print "Sinais vitais. temperatura: 36,8°C, batimento cardíaco: 114 batidas por minuto, ritmo respiratório: 24 " \
          "por minuto. Imagem das lesões corporais aparecerão ao lado. Você pode fechar a imagem quando quiser."
    get_voice_from_this("resp_ef")
    img = Image.open(dir_files + "exame1.png")
    img.show()

def resp_exame_lab():
    print "A imagem do exame aparecerá ao lado. Você pode fechar a imagem quando quiser"
    get_voice_from_this("resp_lab")
    img = Image.open(dir_files + "exame_lab.png")
    img.show()

def resp_exame_extra():
    print "Um ecocardiograma revelou um discreto aumento do ventrículo esquerdo com função diminuída, fração de ejeção " \
          "estimada em 30% sendo o normal acima de 60%. UM raio X do peito demonstra um edema pulmonar."
    get_voice_from_this("resp_extra")

def get_caso_real():
    print "Início do caso. Uma estudante universitária de dezoito anos chega ao seu consultório, sua principal queixa " \
          "é dor de cabeça e erupção cutânea"
    get_voice_from_this("paciente")
    print "Fale qual das possíveis informações você deseja para fazer um diagnóstico:"
    get_voice_from_this("csm_intro")
    print "1 - Histórico de doenças presentes atualmente"
    get_voice_from_this("csm_hp")
    print "2 - Histórico médico"
    get_voice_from_this("csm_hm")
    print "3 - Histórico familiar"
    get_voice_from_this("csm_hf")
    print "4 - Exame físico"
    get_voice_from_this("csm_ef")
    print "5 - Exame laboratorial"
    get_voice_from_this("csm_lab")
    print "6 - Exame extra"
    get_voice_from_this("csm_extra")
    get_voice_from_this("get_pronto")
    while True:
        resp = get_open_question()
        print "Fale qual das possíveis informações você deseja para fazer um diagnóstico:"
        print "1 - Histórico de doenças presentes atualmente"
        print "2 - Histórico médico"
        print "3 - Histórico familiar"
        print "4 - Exame físico"
        print "5 - Exame laboratorial"
        print "6 - Exame extra"
        if "sair" in resp:
            break
        elif u"histórico de doenças" in resp:
            resp_hist_doenca()
            get_voice_from_this("get_pronto")
        elif u"histórico médico" in resp:
            resp_hist_medico()
            get_voice_from_this("get_pronto")
        elif u"histórico familiar" in resp:
            resp_hist_familiar()
            get_voice_from_this("get_pronto")
        elif u"exame físico" in resp:
            resp_exam_fisico()
            get_voice_from_this("get_pronto")
        elif u"exame laboratorial" in resp:
            resp_exame_lab()
            get_voice_from_this("get_pronto")
        elif u"exame extra" in resp:
            resp_exame_extra()
            get_voice_from_this("get_pronto")
        elif any(word in resp for word in [u"pronto", u"diagnóstico"]):
            resp_diagnostico()
        else:
            print("Desculpe, não entendi")
            msg_dont_get_it()
            time.sleep(1.0)
