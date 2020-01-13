suits='H D C S'.split()
ranks='2 3 4 5 6 7 8 9 10 J Q K A'.split()
cards=[]

for i in suits:
    for j in ranks:
        cards.append(i+" "+j)

import random
random.shuffle(cards)

deckc=cards[:26]
decku=cards[26:]
print("****WELCOME TO THE WAR -- THE ULTIMATE CARD GAME****")
print("$$$$$ Its a game between You and Computer $$$$$")


class Player():

    def __init__(self,name):
        self.name=name
you=Player(input("Enter your name:"))
print(you.name)


Decku=[]
for i in decku:
    if i.split()[1] == 'J':
        Decku.append(i.split()[0]+" "+'11')
    elif i.split()[1] == 'Q':
        Decku.append(i.split()[0]+" "+'12')
    elif i.split()[1] == 'K':
        Decku.append(i.split()[0]+" "+'13')
    elif i.split()[1] == 'A':
        Decku.append(i.split()[0]+" "+'14')
    else:
        Decku.append(i)

Deckc=[]
for i in deckc:
    if i.split()[1] == 'J':
        Deckc.append(i.split()[0]+" "+'11')
    elif i.split()[1] == 'Q':
        Deckc.append(i.split()[0]+" "+'12')
    elif i.split()[1] == 'K':
        Deckc.append(i.split()[0]+" "+'13')
    elif i.split()[1] == 'A':
        Deckc.append(i.split()[0]+" "+'14')
    else:
        Deckc.append(i)

print("Lets the WAR begin!")
print("THE TWO RANDOM PACK IS BELOW")
print("PACK OF COM---",deckc)
print("length of Deckc: ",len(deckc))
print("PACK OF YOU---",decku)
print("length of Decku: ",len(decku))


key=input(" ARE YOU READY TO BEGIN THE BATTLE OF CARDS : ")
ct=0
rounds=0
if key == "Y" or key=="y":
    while not len(Decku)==0 or len(Deckc)==0:
        rounds=rounds+1

        if len(Deckc)<=3 or len(Decku)<=3:
            print("last round results")
            print("YOUR PACK : ",Decku)
            print("COMP PACK : ",Deckc)
            if len(Decku)>len(Deckc):
                Deckc=[]
                break
            else:
                Decku=[]
                break


        if int(Decku[ct].split()[1]) > int(Deckc[ct].split()[1]):
            Decku.append(Decku[ct].split()[0]+" "+Decku[ct].split()[1])
            Decku.append(Deckc[ct].split()[0]+" "+Deckc[ct].split()[1])
            del Decku[ct]
            del Deckc[ct]
            ct=0

        elif int(Deckc[ct].split()[1]) > int(Decku[ct].split()[1]):
            Deckc.append(Deckc[ct].split()[0]+" "+Deckc[ct].split()[1])
            Deckc.append(Decku[ct].split()[0]+" "+Decku[ct].split()[1])
            del Deckc[ct]
            del Decku[ct]
            ct=0

        elif int(Deckc[ct].split()[1]) == int(Decku[ct].split()[1]):
                ct=ct+2
                if int(Decku[ct].split()[1]) > int(Deckc[ct].split()[1]):
                    Decku.append(Decku[ct].split()[0]+" "+Decku[ct].split()[1])
                    Decku.append(Deckc[ct].split()[0]+" "+Deckc[ct].split()[1])
                    Decku.append(Deckc[ct-1].split()[0]+" "+Deckc[ct-1].split()[1])
                    Decku.append(Deckc[ct-2].split()[0]+" "+Deckc[ct-2].split()[1])
                    Decku.append(Deckc[ct-3].split()[0]+" "+Deckc[ct-3].split()[1])
                    del Decku[ct]
                    del Deckc[ct]
                    del Deckc[ct-1]
                    del Deckc[ct-2]
                    del Deckc[ct-3]
                    ct=0
                elif int(Deckc[ct].split()[1]) > int(Decku[ct].split()[1]):
                    Deckc.append(Deckc[ct].split()[0]+" "+Deckc[ct].split()[1])
                    Deckc.append(Decku[ct].split()[0]+" "+Decku[ct].split()[1])
                    Deckc.append(Decku[ct-1].split()[0]+" "+Decku[ct-1].split()[1])
                    Deckc.append(Decku[ct-2].split()[0]+" "+Decku[ct-2].split()[1])
                    Deckc.append(Decku[ct-3].split()[0]+" "+Decku[ct-3].split()[1])
                    del Deckc[ct]
                    del Decku[ct]
                    del Decku[ct-1]
                    del Decku[ct-2]
                    del Decku[ct-3]
                    ct=0



    if len(Deckc)==0 or len(Decku)==52:
        print("WINNER!! WINNER!! THE WARRIOR---",you.name.upper())
    else:
        print("YOU LOST THE BATTLE!!")
    print("Total Rounds played:",rounds)
else:
    print("Let's do another time!!")
    exit()
