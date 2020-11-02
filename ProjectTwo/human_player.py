import card2

def discard(hand):
    temp = 0
    if(hand == []):
        print("List is Empty!")
    else:
        for tempHand in hand:
            print(str(temp) + "          " + card2.card_to_string(tempHand))
            temp += 1
        tempInput = int(input("Choice: "))
        return hand[tempInput]

def draw(hand, top_discard_card):
    tempInputD = input("Draw location: ")
    if(tempInputD.lower() == "stock" or tempInputD.lower() == "discard"):
        return tempInputD
    else:
        return "Wrong Draw Location!"

print(draw([4, 50, 15, 21], None))