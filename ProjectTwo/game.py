import card1

def calculate_winner(points):
    listMin = []
    if(points == []):
        print("List is Empty!")
    else:
        tempMin = min(points)
        for i in range(len(points)):
            if(tempMin == points[i]):
                listMin.append(i)
        return listMin

def calculate_round_points(hand):
    if(hand == []):
        print("List is Empty!")
    else:
        count = 0
        for tempHand in hand:
            tempPoints = card1.get_rank(tempHand)
            if(tempPoints < 9):
                count += (tempPoints + 2)
            elif(tempPoints > 8 and tempPoints > 12):
                count += 10
            else:
                count += 1
        
        return count

def is_valid_group(cards):
    if(cards == []):
        print("List is Empty!")
    else:
        for i in range(0, len(cards)):
            for j in range(i+1, len(cards)):
                if(card1.same_rank(cards[i], cards[j]) == False):
                    return False
        return True

def is_valid_sequence(cards):
    if(cards == []):
        print("List is Empty!")
    else:
        for i in range(0, len(cards)):
            for j in range(i+1, len(cards)):
                if(card1.same_suit(cards[i], cards[j]) == False):
                    return False
        return True
    