from random import randint

text = input("Zieltext eingeben:")
versuch = []
richtig = []
gen = 0

for i in text:
    versuch.append("")
    
while text != "".join(versuch):

    for i,char in enumerate(text):
        if versuch[i] == char:
            richtig.append(versuch[i])
        else:
            versuch[i] = chr(randint(0, 255))
        gen += 1
    print("".join(versuch))

print(gen)

    
