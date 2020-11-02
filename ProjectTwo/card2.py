import card1

SUITS_STR = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
RANKS_STR = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN","EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]

def get_card(suits, ranks):
    if(type(suits) == int and type(ranks) == int):
        if(suits >= 0 and suits < 5):
            if(ranks >= 0 and suits < 13):
                return ((ranks * 4) + (suits + 1))
            else:
                print("Wrong value!")
        else:
             print("Wrong value!")
    elif(type(suits) == str and type(ranks) == str):
        if(suits.upper() in SUITS_STR):
            tempSuits = SUITS_STR.index(suits)
            if(ranks.upper() in RANKS_STR):
                tempRanks = RANKS_STR.index(ranks)
                return ((tempRanks * 4) + (tempSuits + 1))
            else:
                print("Wrong value!")
        else:
              print("Wrong value!")
    else:
        print("Wrong value!")

def card_to_string(card):
    if(card < 53 and card > 0):
        return RANKS_STR[card1.get_rank(card)] + " of " + SUITS_STR[card1.get_suit(card)]
    else:
        print("Out Of Range!")
    
def hand_to_string(hand):
    strHand = ""
    if(hand == []):
        print("List is Empty!")
    else:
        for tempList in hand:
            strHand += card_to_string(tempList)
            if(tempList != hand[-1]):
                strHand += ", "
    return strHand

def get_deck():
    listDeck = []
    for i in RANKS_STR:
        for j in SUITS_STR:
            listDeck.append( i + " of " + j)
    return listDeck

def all_same_suit(cards):
    if(cards == []):
        print("List is Empty!")
    else:
        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if(card1.same_suit(cards[i],cards[j]) == False):
                    return False
    return True

def all_same_rank(cards):
    if(cards == []):
        print("List is Empty!")
    else:
        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if(card1.same_rank(cards[i],cards[j]) == False):
                    return False
    return True

        
        