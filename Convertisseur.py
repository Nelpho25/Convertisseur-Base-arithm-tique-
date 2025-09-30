import tkinter as tk
#constantes
baseactuelle=10
nombre="0"

#fonction de changement de base
def deDecimal (nombre , base ,actubase):
    nombre=int(nombre,actubase) #transforme le nombre qui est dans la base actubase sous la forme d un entier
    chiffres ="0123456789ABCDEF"
    ch=""
    while nombre>0:
        ch=chiffres[nombre%base]+ch
        nombre=nombre//base
    actubase=base

    return ch

#definition des variable des bases

def base2action ():
    global nombre
    global baseactuelle
    ch=deDecimal (nombre ,2,baseactuelle)
    nombre=ch
    baseactuelle=2
    resultat.config(text = nombre)
    base16['bg'] = couleurPrincipale
    base10['bg'] = couleurPrincipale
    base2['bg'] = 'grey'
    Bouton2['fg'] = 'grey'
    Bouton3['fg'] = 'grey'
    Bouton4['fg'] = 'grey'
    Bouton5['fg'] = 'grey'
    Bouton6['fg'] = 'grey'
    Bouton7['fg'] = 'grey'
    Bouton8['fg'] = 'grey'
    Bouton9['fg'] = 'grey'
    BoutonA['fg'] = 'grey'
    BoutonB['fg'] = 'grey'
    BoutonC['fg'] = 'grey'
    BoutonD['fg'] = 'grey'
    BoutonE['fg'] = 'grey'
    BoutonF['fg'] = 'grey'
    return

def base10action():
    global nombre
    global baseactuelle
    ch=deDecimal (nombre ,10,baseactuelle)
    nombre=ch
    baseactuelle=10
    resultat.config(text = nombre)
    resultat.config(text = nombre)
    base16['bg'] = couleurPrincipale
    base10['bg'] = 'grey'
    base2['bg'] = couleurPrincipale
    Bouton2['fg'] = couleurSecondaire
    Bouton3['fg'] = couleurSecondaire
    Bouton4['fg'] = couleurSecondaire
    Bouton5['fg'] = couleurSecondaire
    Bouton6['fg'] = couleurSecondaire
    Bouton7['fg'] = couleurSecondaire
    Bouton8['fg'] = couleurSecondaire
    Bouton9['fg'] = couleurSecondaire
    BoutonA['fg'] = 'grey'
    BoutonB['fg'] = 'grey'
    BoutonC['fg'] = 'grey'
    BoutonD['fg'] = 'grey'
    BoutonE['fg'] = 'grey'
    BoutonF['fg'] = 'grey'
    return

def base16action():
    global nombre
    global baseactuelle
    ch=deDecimal (nombre ,16,baseactuelle)
    nombre=ch
    baseactuelle=16
    resultat.config(text = nombre)
    resultat.config(text = nombre)
    base16['bg'] = 'grey'
    base10['bg'] = couleurPrincipale
    base2['bg'] = couleurPrincipale
    Bouton2['fg'] = couleurSecondaire
    Bouton3['fg'] = couleurSecondaire
    Bouton4['fg'] = couleurSecondaire
    Bouton5['fg'] = couleurSecondaire
    Bouton6['fg'] = couleurSecondaire
    Bouton7['fg'] = couleurSecondaire
    Bouton8['fg'] = couleurSecondaire
    Bouton9['fg'] = couleurSecondaire
    BoutonA['fg'] = couleurSecondaire
    BoutonB['fg'] = couleurSecondaire
    BoutonC['fg'] = couleurSecondaire
    BoutonD['fg'] = couleurSecondaire
    BoutonE['fg'] = couleurSecondaire
    BoutonF['fg'] = couleurSecondaire
    return

#definitions des variables des bouttons
def BoutonResetAction():
    global nombre

    nombre="0"
    resultat.config(text = nombre)

def ajoutChiffre (chiffre):
    global nombre
    if nombre =="0" :
        nombre =chiffre
    else :
        nombre=nombre+chiffre
    resultat.config(text = nombre)
    return

def Bouton0action ():
    ajoutChiffre ("0")
    return

def Bouton1action ():
    ajoutChiffre ("1")
    return

def Bouton2action ():
    if baseactuelle >2:
        ajoutChiffre ("2")
    return

def Bouton3action ():
    if baseactuelle >2:
        ajoutChiffre ("3")
    return
def Bouton4action ():
    if baseactuelle >2:
        ajoutChiffre ("4")
    return

def Bouton5action ():
    if baseactuelle >2:
        ajoutChiffre ("5")
    return
def Bouton6action ():
    if baseactuelle >2:
        ajoutChiffre ("6")
    return

def Bouton7action ():
    if baseactuelle >2:
        ajoutChiffre ("7")
    return

def Bouton8action ():
    if baseactuelle >2:
        ajoutChiffre ("8")
    return

def Bouton9action ():
    if baseactuelle >2:
        ajoutChiffre ("9")
    return

def BoutonAaction ():
    if baseactuelle >10:
        ajoutChiffre ("A")
    return

def BoutonBaction ():
    if baseactuelle >10:
        ajoutChiffre ("B")
    return

def BoutonCaction ():
    if baseactuelle >10:
        ajoutChiffre ("C")
    return

def BoutonDaction ():
    if baseactuelle >10:
        ajoutChiffre ("D")
    return

def BoutonEaction ():
    if baseactuelle >10:
        ajoutChiffre ("E")
    return

def BoutonFaction ():
    if baseactuelle >10:
        ajoutChiffre ("F")
    return
#varaiable aspect graphique
police="Arial"
tailleBouttons=25
tailleresultat=tailleBouttons*1

hauteurreset=10000


hauteurboutton=1
largeurboutton=1

hauteurbase=1
largeurbase=12

hauteurresultat=1
largeurresultat=1000

couleurPrincipale="black"
couleurSecondaire="white"
taillebordure=3

#creation de la fenetre

window =tk.Tk()

#caractéristique de la fenetre

window.title (" Calculatrice ")
window.geometry("500x400")
window.minsize(400,400)
#window.maxsize(400,600)
window.config(background=couleurPrincipale)

#creation frame
frameBoutton= tk.Frame(window,bg=couleurPrincipale,bd=-1,relief="groove")
frameResultat= tk.Frame(window,bg=couleurPrincipale,bd=-1,relief="groove")

#creation sous frame pour boutons
frameChiffres=tk.Frame(frameBoutton,bg=couleurPrincipale)
frameBase=tk.Frame(frameBoutton,bg=couleurPrincipale)

#sous sous fenetre pour repartietion des bouttons
frameReset=tk.Frame(frameChiffres,bg=couleurPrincipale)
frameChiffresGauche=tk.Frame(frameChiffres,bg=couleurPrincipale)
frameChiffresMillieu=tk.Frame(frameChiffres,bg=couleurPrincipale)
frameChiffresDroites=tk.Frame(frameChiffres,bg=couleurPrincipale)


#affichage resultat
resultat = tk.Label(frameResultat,text = nombre,font=(police,tailleresultat),bg=couleurPrincipale,fg=couleurSecondaire, height=hauteurresultat, width =largeurresultat)

resultat.pack(side="right",fill="x")

#creation bases
base2 = tk.Button(frameBase, text = "Binnaire", font=(police,tailleBouttons), height=hauteurbase, width =largeurbase, bg = couleurPrincipale , fg = couleurSecondaire , bd = taillebordure , relief = "groove",command=base2action)
base2.pack(expand="yes")

base10 = tk.Button(frameBase, text = "Décimales", font=(police,tailleBouttons), height=hauteurbase, width =largeurbase, bg = "gray" , fg = couleurSecondaire , bd = taillebordure , relief = "groove",command=base10action)
base10.pack(expand="yes")

base16 = tk.Button(frameBase, text = "Hexadécimales", font=(police,tailleBouttons), height=hauteurbase, width =largeurbase, bg = couleurPrincipale , fg = couleurSecondaire , bd = taillebordure , relief = "groove",command=base16action)
base16.pack(expand="yes")

#affichage reset
reset = tk.Button(frameBase,text = "Reset",font=(police,tailleBouttons),height=hauteurbase, width =largeurbase,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove",command = BoutonResetAction)

reset.pack(expand="yes")

#creation chiffres
Bouton0 = tk.Button(frameReset, text = "0", font=(police,tailleBouttons), height=hauteurboutton, width =largeurboutton*8, bg = couleurPrincipale , fg = couleurSecondaire , bd = taillebordure , relief = "groove", command = Bouton0action )

Bouton0.pack(side="left")

Bouton1 = tk.Button(frameChiffresGauche, text = "1", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton1action)
Bouton1.pack(side="left")


Bouton2 = tk.Button(frameChiffresGauche, text = "2", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton2action)
Bouton2.pack(side="left")


Bouton3 = tk.Button(frameChiffresGauche, text = "3", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton3action)
Bouton3.pack(side="left")

Bouton4 = tk.Button(frameChiffresGauche, text = "4", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton4action)
Bouton4.pack(side="left")


Bouton5 = tk.Button(frameChiffresGauche, text = "5", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton5action)
Bouton5.pack(side="left")


Bouton6 = tk.Button(frameChiffresMillieu, text = "6", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton6action)
Bouton6.pack(side="left")


Bouton7 = tk.Button(frameChiffresMillieu, text = "7", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton7action)
Bouton7.pack(side="left")


Bouton8 = tk.Button(frameChiffresMillieu, text = "8", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton8action)
Bouton8.pack(side="left")





Bouton9 = tk.Button(frameChiffresMillieu, text = "9", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg=couleurSecondaire,bd=taillebordure,relief="groove", command = Bouton9action)
Bouton9.pack(side="left")

BoutonA = tk.Button(frameChiffresMillieu, text = "A", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonAaction)
BoutonA.pack(side="left")

BoutonB = tk.Button(frameChiffresDroites, text = "B", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonBaction)
BoutonB.pack(side="left")

BoutonC = tk.Button(frameChiffresDroites, text = "C", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonCaction)
BoutonC.pack(side="left")

BoutonD = tk.Button(frameChiffresDroites, text = "D", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonDaction)
BoutonD.pack(side="left")

BoutonE = tk.Button(frameChiffresDroites, text = "E", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonEaction)
BoutonE.pack(side="left")

BoutonF = tk.Button(frameChiffresDroites, text = "F", font=(police, tailleBouttons), height=hauteurboutton, width =largeurboutton,bg=couleurPrincipale,fg='grey',bd=taillebordure,relief="groove",command =BoutonFaction)
BoutonF.pack(side="left")

#affichage

frameReset.pack(side="bottom")
frameBase.pack(side="right")
frameChiffresDroites.pack(side="bottom")
frameChiffresGauche.pack(side="top")
frameChiffresMillieu.pack(expand="yes")


frameBoutton.pack(side="bottom")
frameResultat.pack(side="right",)

frameChiffres.pack(side="bottom")



window.mainloop()
