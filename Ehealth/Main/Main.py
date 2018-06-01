# -*- coding: utf-8 -*-#

'''
Created on 24 de mai de 2018

@author: lucas
'''


import Kassandra.Kassandra as ka



if __name__ == '__main__':
    cont = 1
    ka.msg_conf()
    ka.conf()
    ka.get_intro() 
    while True:
        if cont<2:ka.general_menu()
        else: ka.short_general_menu()
        opt = ka.get_open_question()
        if "sair" in opt: break
        elif "meningite" in opt:
            ka.get_meningite()
            cont+=1
            break
        else: 
            print "O que deseja saber?"
            result = ka.get_search(opt)
            if result:
                ka.waiting_ask()
                cont+=1
    
    mens = ("Obrigado e até mais.")
    print ("Obrigado e até mais.")
    ka.tell_this_file(mens, "tchau",)    
        
    
    