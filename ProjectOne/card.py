#SUIT
HEARTS = 0      #RED
DIAMONDS = 1    #RED
CLUBS = 2       #BLACK
SPADES = 3      #BLACk

#RANK
TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

def get_suit(card):
    return int((card % 4) - 1)       #Suit 4 oldugu için 4 e göre mod alarak hangi suit oldugunu bulabşliriz -1 sebebi ise 0 danbaslıyor
def get_rank(card):
    return int((card / 4))           #Burada 4'e göremod alarak hangi dörtlüde olduğunu buluyoruz

def same_suit(card1, card2):
    if(get_suit(card1) == get_suit(card2)):
        return True
    else:
        return False

def same_rank(card1, card2):
    if(get_rank(card1) == get_rank(card2)):
        return True
    else:
        return False
    
def same_color_suit(card1, card2):
    suit1 = get_suit(card1)         #Hazır fonksiyonları kullandık
    suit2 = get_suit(card2)
    
    if(suit1 == suit2):
        return True
    else:
        if(suit1<2 and suit2<2):
            return True
        elif(suit1>1 and suit2>1):
            return True
        else:
            return False
        
        
        
        
print(get_suit(25))
print(get_rank(19))
print(same_rank(11, 32))
print(same_suit(17, 33))
print(same_color_suit(35, 7))