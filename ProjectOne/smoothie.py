SMOOTHIE1_NAME = "Strawberry Smoothie"
SMOOTHIE2_NAME = "Banana Smoothie"
SMOOTHIE3_NAME = "Pineapple Smoothie"
SMOOTHIE4_NAME = "Onion Toffee Smoothie"
SMOOTHIE1_POST = 5.0
SMOOTHIE2_POST = 6.5
SMOOTHIE3_POST = 7.5
SMOOTHIE4_POST = 8.0
SIZE1_NAME = "Small"
SIZE2_NAME = "Medium"
SIZE3_NAME = "Large"
SIZE4_NAME = "Galactic"
SIZE1_COST = -2.0
SIZE2_COST = 0.0
SIZE3_COST = 2.5
SIZE4_COST = 4.0
TOPPIC1_NAME = "No Topping"
TOPPIC2_NAME = "Chocolate"
TOPPIC3_NAME = "Raspberry"
TOPPIC4_NAME = "Caramel"
TOPPIC1_COST = 0.0
TOPPIC2_COST = 1.5
TOPPIC3_COST = 1.5
TOPPIC4_COST = 1.5



def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4,  cost4):
    print(question)
    print("1)     "+"$"+str(cost1)+"     "+option1)
    print("2)     "+"$"+str(cost2)+"     "+option2)
    print("3)     "+"$"+str(cost3)+"     "+option3)
    print("4)     "+"$"+str(cost4)+"     "+option4)
    
    inputP = input("Your choice (1-4): ")
    if(inputP == "1" or inputP == "2" or inputP == "3" or inputP == "4"):       #bir ile 4 arası girmesini saglıyor
        return inputP
    else:
        return 0

def calculate_subtotal(smoothie_type, smoothie_size, topping):
    calculate = 0
    
    calculate += SMOOTHIE4_POST                 #herzaman soğanlı verdiğimiz icin direkt onu hesaba katıyoruz
    
    if(smoothie_size == SIZE1_NAME):            #duruma göre size fiyatını katıyoruz
        calculate += SIZE1_COST
    elif(smoothie_size == SIZE2_NAME):
        calculate += SIZE2_COST
    elif(smoothie_size == SIZE3_NAME):
        calculate += SIZE3_COST
    else:
        calculate += SIZE4_COST
        
    if(topping == TOPPIC1_NAME):                #duruma göre topic ekliyoruz
        calculate += TOPPIC1_COST
    elif(topping == TOPPIC2_NAME):
        calculate += TOPPIC2_COST
    elif(topping == TOPPIC3_NAME):
        calculate += TOPPIC3_COST
    else:
        calculate += TOPPIC4_COST
    
    return calculate

def print_receipt(subtotal, smoothie_type, smoothie_size, topping):                 #hersey burada yazdırılıyor
    print("You ordered a "+smoothie_size+" "+smoothie_type+" with "+topping)
    print("Smoothie cost: "+str(subtotal))
    tempQst = round(subtotal * (0.09975),2)             #round virgurden sonra iki basamak eklememize yarıyor. Standart python kütüphanesidir
    print("QST:     $"+str(tempQst))
    tempGst = round(subtotal * (0.05),2)
    print("GST:     $"+str(tempGst))
    total = round(subtotal + tempGst + tempQst,2)
    print("Total    $"+str(total))
    
    return total
    

def order():
    print("Welcome to Smooth Smoothies Smoothie Ordering System")
    print("Have you tried our new Onion Toffee smoothie?")
    print("Which smoothie would you like?")
    print("1)     "+"$"+str(SMOOTHIE1_POST)+"     "+SMOOTHIE1_NAME)
    print("2)     "+"$"+str(SMOOTHIE2_POST)+"     "+SMOOTHIE2_NAME)
    print("3)     "+"$"+str(SMOOTHIE3_POST)+"     "+SMOOTHIE3_NAME)
    print("4)     "+"$"+str(SMOOTHIE4_POST)+"     "+SMOOTHIE4_NAME)
    
    inputS = input("Your choice (1-4): ")
    
    if(inputS == "1" or inputS == "2" or inputS == "3" or inputS == "4"):
        if(inputS == "1"):
            print("You have selected "+SMOOTHIE1_NAME)
            print("Unfortunately, we are out of "+SMOOTHIE1_NAME)
            print("You will be served "+SMOOTHIE4_NAME)
            tempST = SMOOTHIE4_NAME
        elif(inputS == "2"):
            print("You have selected "+SMOOTHIE2_NAME)
            print("Unfortunately, we are out of "+SMOOTHIE2_NAME)
            print("You will be served "+SMOOTHIE4_NAME)
            tempST = SMOOTHIE4_NAME
        elif(inputS == "3"):
            print("You have selected "+SMOOTHIE3_NAME)
            print("Unfortunately, we are out of "+SMOOTHIE3_NAME)
            print("You will be served "+SMOOTHIE4_NAME)
            tempST = SMOOTHIE4_NAME
        else:
             print("You have selected "+SMOOTHIE4_NAME)
             tempST = SMOOTHIE4_NAME
             
        inputSize = pose_question_with_costs("Which size would you like?", SIZE1_NAME, SIZE1_COST, SIZE2_NAME, SIZE2_COST, SIZE3_NAME, SIZE3_COST, SIZE4_NAME,  SIZE4_COST)
        if(inputSize == 0):
            print("Sorry, that is not a valid option.")
        else:
            if(inputSize == "1"):
                print("You have selected "+SIZE1_NAME)
                tempS = SIZE1_NAME
            elif(inputSize == "2"):
                print("You have selected "+SIZE2_NAME)
                tempS = SIZE2_NAME
            elif(inputSize == "3"):
                print("You have selected "+SIZE3_NAME)
                tempS = SIZE3_NAME
            else:
                print("You have selected "+SIZE4_NAME)
                tempS = SIZE4_NAME
            inputTopic = pose_question_with_costs("Which topping would you like?", TOPPIC1_NAME, TOPPIC1_COST, TOPPIC2_NAME, TOPPIC2_COST, TOPPIC3_NAME, TOPPIC3_COST, TOPPIC4_NAME,  TOPPIC4_COST)
            if(inputTopic == 0):
                print("Sorry, that is not a valid option.")
            else:
                if(inputTopic == "1"):
                    print("You have selected "+TOPPIC1_NAME)
                    tempT = TOPPIC1_NAME
                elif(inputTopic == "2"):
                    print("You have selected "+TOPPIC2_NAME)
                    tempT = TOPPIC2_NAME
                elif(inputTopic == "3"):
                    print("You have selected "+TOPPIC3_NAME)
                    tempT = TOPPIC3_NAME
                else:
                    print("You have selected "+TOPPIC4_NAME)
                    tempT = TOPPIC4_NAME
                
                
                subTotalM = calculate_subtotal(tempST, tempS, tempT)
                totalM = print_receipt(subTotalM, tempST, tempS, tempT)
                
                
    else:
        print("Sorry, that is not a valid option.")
    
order()