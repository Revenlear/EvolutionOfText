#EvolutionOfText.py v1.1            Malte Grunert, 12.01.15
#Programm "errät" einen Input, und gibt dann die Anzahl der Versuche aus

from random import randint

#Variablen werden erstellt
text = input("Zieltext eingeben:")      #Zu erratender Input
versuch = []                            #Aktueller Versuch
gen = 0                                 #Anzahl an Versuchen

#Initialisiere versuch --> Wichtig für korrekte Anzahl an Iterationen
for i in text:
    versuch.append("")

#Solange richtig nicht gleich test ist; d.h. solange das Wort noch nicht erraten ist
while text != "".join(versuch):

    #Iteriert über text (i = index; char = wert)
    for i,char in enumerate(text):
        #Wenn versuch an der momentanen stelle identisch mit char ist, tue nichts
        if versuch[i] == char:
            pass
        #Sonst setze einen zufälligen Buchstaben ein
        else:
            versuch[i] = chr(randint(0, 255))
    #Erhöhe die Anzahl an Versuchen
    gen += 1
    #Gib den aktuellen Versuch aus; letzter ist automatisch richtig
    print("".join(versuch))

#Gib die Anzahl an Versuchen aus
print(gen)

#Idee: http://usingpython.com/programs/#evolution   
