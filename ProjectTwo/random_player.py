import random

def draw(hand, top_discard_card):
    if(top_discard_card == None):
        return "stock"
    else:
        rand = random.randint(0,1)
        if(rand == 0):
            return "stock"
        else:
            return "discard"

def discard(hand):
    rand = random.randint(0,len(hand)-1)
    return hand[rand]