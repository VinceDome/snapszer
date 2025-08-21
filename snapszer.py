import random, os, math


colors =  ["t", "m", "p", "z"]
values = [2, 3, 4, 10, 11]



playerCards = []
opponentCards = []
adu = []
lehúzás = False

def switch(input):
    
    if input == 0:
        return 1
    elif input == 1:
        return 0
    
def ExtractCard(raw):
    card = []
    for i in colors:
        if i in raw:
            card.append(i)
            break

    for i in values:
        if str(i) in raw:
            card.append(int(i))
            break
    if len(card) == 2:
        return card
    else:
        return []


while adu == []:
    adu = ExtractCard(input("Mi az adu? "))
    if adu == []:
        print("Helytelen adu")
    

for i in range(5):
    while True:
        card = ExtractCard(input(f"{i+1}. kártya? "))
        if card == adu or card in playerCards or card == []:
            print("Ez a kártya már van/helytelen")
        else:
            break
    playerCards.append(card)

while True:
    try:
        starter = int(input("Ki kezd?\n0 = te /// 1 = ellenfél "))
        if starter not in [0, 1]:
            raise "xddd"
        break
    except:
        print("lmao no")




unseen = []
for i in colors:
    for a in values:
        unseen.append([i, a])


unseen.remove(adu)
for i in playerCards:
    unseen.remove(i)




def SpecificCard(card):
    global unseen, playerCards, opponentCards, adu
    if card in playerCards:
        return "it's in your hand"
    elif card in opponentCards:
        return "100%"
    elif card == adu:
        return "it's the adu"
    elif card in unseen:
        return str(round(((5-len(opponentCards))/len(unseen))*100))+"%"
    else:
        return "lmao kiment"
    
def SpecificColor(color):
    global unseen, playerCards, opponentCards, adu
    for i in opponentCards:
        if i[0] == color:
            return "100%"
    count = 0
    for i in unseen:
        if i[0] == color:
            count += 1

    N = len(unseen)
    n = 5-len(opponentCards)

    print(count, N, n)
    p = 1-(math.comb(N-count, n)/math.comb(N, n))
    return str(round(p*100))+"%"

hits = [[], []]
turn = 0
while True:
    command = input(f"Adu: {adu}\nYour cards are: {playerCards} --- Your points: {sum(i[1] for i in hits[0])}\nYour opponent's cards are: {opponentCards} --- Opponent points: {sum(i[1] for i in hits[1])}\nStarter player is {starter} btw ").split(" ")
    os.system("clear")
    if command[0] == "p":
        card = ExtractCard(command[1])
        if card != []:
            print(SpecificCard(card))
        else:
            print(SpecificColor(command[1]))
    else:
        card = ExtractCard(command[0])
        if card != []:
            play = []
            if card == adu:
                if starter == 0:
                    alsó = [adu[0], 2]
                    if alsó in playerCards:
                        playerCards.remove(alsó)
                        playerCards.append(adu)
                        adu = alsó
                        print("switched")
                    else:
                        print("not valid switcherooo ")
                        continue
                else:
                    opponentCards.append(adu)
                    adu = [adu[0], 2]
                    unseen.remove(adu)

                continue
            elif card in playerCards:
                if starter == 0:
                    playerCards.remove(card)
                    play.append(card)
                else:
                    print("wtf it's in your hand")
                    continue
            else:
                if starter == 1:
                    try:
                        opponentCards.remove(card)
                    except:
                        unseen.remove(card)
                    play.append(card)
                else:
                    print("wtf it's not in your hand")
                    continue

            #reply should be made
            while True:
                card = ExtractCard(input("Reply? "))
                if card != []:
                    break
            
            if card is adu:
                print("wtf it's adu")
                continue
            elif card in playerCards:
                if starter == 1:
                    playerCards.remove(card)
                    play.append(card)
                else:
                    print("wtf it's in your hand")
                    continue
            else:
                if starter == 0:
                    try:
                        opponentCards.remove(card)
                    except:
                        unseen.remove(card)
                    play.append(card)
                else:
                    print("wtf it's not in your hand")
                    continue
            
            if play[0][0] == play[1][0]:
                if play[0][1] > play[1][1]:
                    winner = starter
                else:
                    winner = switch(starter)
            elif play[1][0] == adu[0]:
                winner = switch(starter)
            else:
                winner = starter
            
            for i in play:
                hits[winner].append(i)
            
           
            while True:
                if turn == 4:
                    if winner == 1:
                        playerCards.append(adu)
                        print("Auto-pulled adu")
                        break
                    elif winner == 0:
                        opponentCards.append(adu)
                

                card = ExtractCard(input("What did you pull? "))
                if card != []:
                    playerCards.append(card)
                    unseen.remove(card)
                    break

            starter = winner


        else:
            print("bro it's really not valid")
        
        if turn == 4:
            for i in unseen:
                opponentCards.append(i)
                unseen.remove(i)
            lehúzás = True

        turn += 1



            
                

        


            
        