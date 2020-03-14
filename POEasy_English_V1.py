import keyboard
from tkinter import *
import time
import random

#Creation de la fenetre
window = Tk()
#Personnalisation de la fenetre
window.title("POEasy")
window.minsize(480, 360)
window.config(background="black")



#Fonction affichage selection TBas_______________________________________________________________
                
def returnEntryTb(arg=None):
    global current_resultTb
    global bas
    result = myEntryTb.get()
    resultLabelTb.config(text="Random min delay will be : " + result + " millisecond")
  
    current_resultTb = result
    bas = int(current_resultTb)
    print(current_resultTb)
    myEntryTb.delete(0,END)

    #Ajout du texte T
label_titleTb = Label(window, text="Random min delay  (millisecond) : ", font="Courrier", bg="black", fg='white')
label_titleTb.pack()

# Zone de saisie Tb
myEntryTb = Entry(window, width=20)
myEntryTb.focus()
myEntryTb.bind("<Return>",returnEntryTb)
myEntryTb.pack()

# Bouton valider T
enterEntryTb = Button(window, text= "Confirm / Erase", command=returnEntryTb)
enterEntryTb.pack(fill=X)

# Zone affichage de choix T

resultLabelTb = Label(window, text = "")
resultLabelTb.pack(fill=X)


#Fonction affichage selection THaut_______________________________________________________________
                
def returnEntryTh(arg=None):
    global current_resultTh
    global haut
    result = myEntryTh.get()
    resultLabelTh.config(text="Random max delay will be : " + result + " millisecond")
    current_resultTh = result
    haut = int(current_resultTh)
    print(current_resultTh)
    myEntryTh.delete(0,END)

    #Ajout du texte T
label_titleTh = Label(window, text="Random max delay (millisecond) : ", font="Courrier", bg="black", fg='white')
label_titleTh.pack()

# Zone de saisie Th
myEntryTh = Entry(window, width=20)
myEntryTh.focus()
myEntryTh.bind("<Return>",returnEntryTh)
myEntryTh.pack()

# Bouton valider T
enterEntryTh = Button(window, text= "Confirm / Erase", command=returnEntryTh)
enterEntryTh.pack(fill=X)

# Zone affichage de choix T

resultLabelTh = Label(window, text = "")
resultLabelTh.pack(fill=X)


#Fonction affichage selection R1_______________________________________________________________
                
def returnEntryR1(arg=None):
    global current_resultR1
    result = myEntryR1.get()
    resultLabelR1.config(text="Shortcut S1 defined : " + result)
    current_resultR1 = result
    print(current_resultR1)
    myEntryR1.delete(0,END)

    #Ajout du texte R1
label_titleR1 = Label(window, text="Key defined for the shortcut S1 : ", font="Courrier", bg="black", fg='white')
label_titleR1.pack()

# Zone de saisie R1
myEntryR1 = Entry(window, width=20)
myEntryR1.focus()
myEntryR1.bind("<Return>",returnEntryR1)
myEntryR1.pack()

# Bouton valider R1
enterEntryR1 = Button(window, text= "Confirm / Erase", command=returnEntryR1)
enterEntryR1.pack(fill=X)

# Zone affichage de choix R1

resultLabelR1 = Label(window, text = "")
resultLabelR1.pack(fill=X)


# ______________________________________________________________________________________________
#Fonction affichage selection R2
def returnEntryR2(arg=None):
    global current_resultR2
    result = myEntryR2.get()
    resultLabelR2.config(text="Shortcut S2 defined: " + result)
    current_resultR2 = result
    print(current_resultR2)
    myEntryR2.delete(0,END)

    #Ajout du texte R2
label_titleR2 = Label(window, text="Key defined for the shortcut S2 : ", font="Courrier", bg="black", fg='white')
label_titleR2.pack()

# Zone de saisie R2
myEntryR2 = Entry(window, width=20)
myEntryR2.focus()
myEntryR2.bind("<Return>",returnEntryR1)
myEntryR2.pack()

# Bouton valider R2
enterEntryR2 = Button(window, text= "Confirm / Erase", command=returnEntryR2)
enterEntryR2.pack(fill=X)

# Zone affichage de choix R2

resultLabelR2 = Label(window, text = "")
resultLabelR2.pack(fill=X)

# ______________________________________________________________________________________________
#Fonction affichage selection 1
def returnEntry1(arg=None):
    global current_result1
    global current_result1split
    global current_result1splitOK
    result = myEntry1.get()
    resultLabel1.config(text="Key(s) defined : " + result)
    current_result1 = result
    n = 1
    current_result1split = [current_result1[i:i+n] for i in range(0, len(current_result1), n)]
    current_result1splitOK = ', '.join(current_result1split)
    print(current_result1splitOK)
    myEntry1.delete(0,END)

#Ajout du texte 1
label_title1 = Label(window, text="Key(s) triggered by the shortcut S1 ex (abc&è) : ", font="Courrier", bg="black", fg='white')
label_title1.pack()

# Zone de saisie 1
myEntry1 = Entry(window, width=20)
myEntry1.focus()
myEntry1.bind("<Return>",returnEntry1)
myEntry1.pack()

# Bouton entrer 1
enterEntry1 = Button(window, text= "Confirm / Erase", command=returnEntry1)
enterEntry1.pack(fill=X)
 
 # Zone affichage de choix 1
resultLabel1 = Label(window, text = "")
resultLabel1.pack(fill=X)
#_______________________________________________________________________________________________________________

#Fonction affichage selection 2
def returnEntry2(arg=None):
    global current_result2
    global current_result2split
    global current_result2splitOK
    result = myEntry2.get()
    resultLabel2.config(text="Key(s) defined : " + result)
    current_result2 = result
    n = 1
    current_result2split = [current_result2[i:i+n] for i in range(0, len(current_result2), n)]
    current_result2splitOK = ', '.join(current_result2split)
    print(current_result2splitOK)
    myEntry2.delete(0,END)

#Ajout du texte 2
label_title2 = Label(window, text="Key(s) triggered by the shortcut S2 ex (abc&è) : ", font="Courrier", bg="black", fg='white')
label_title2.pack()

# Zone de saisie 2
myEntry2 = Entry(window, width=20)
myEntry2.focus()
myEntry2.bind("<Return>",returnEntry2)
myEntry2.pack()

# Bouton entrer 2
enterEntry2 = Button(window, text= "Confirm / Erase", command=returnEntry2)
enterEntry2.pack(fill=X)
 
 # Zone affichage de choix 2
resultLabel2 = Label(window, text = "")
resultLabel2.pack(fill=X)

#_______LANCEMENT DU PROGRAMME______________________________________________________________________________________

#Fonctions pour lancer le programme
def lancement1():
    keyboard.add_hotkey(current_resultR1, on_triggered1) #<-- Attache la fonction au raccourci "shortcurt1"
    keyboard.add_hotkey(current_resultR2, on_triggered2) #<-- Attache la fonction au raccourci "shortcurt2" 
    
def on_triggered1(): 
    time.sleep(random.randint(bas, haut)/1000)
    keyboard.press_and_release(current_result1splitOK) #<-- Ecrit le contenu de current_result1

#Fonctions pour Raccourci 2
def on_triggered2(): 
    time.sleep(random.randint(bas, haut)/1000)
    keyboard.press_and_release(current_result2splitOK) #<-- Ecrit le contenu de current_result2



#________BOUTON DE LANCEMENT________________________________________________________________________________________
premier_bouton = Button(window, text="Run", font="Courrier", bg="White", fg='black', command=lancement1)
premier_bouton.pack(pady=25, fill=X)
 
#Aide
label_aide = Label(window, text="Validate all the fields (even if empty) before clicking on run !", font="Courrier", bg="black", fg='red')
label_aide.pack()

window.mainloop()