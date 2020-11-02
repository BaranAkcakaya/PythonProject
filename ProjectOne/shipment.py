def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):              #Tek tek carparak hesaplıyoruz
    checkDigit = (d1 * 1) + (d2 * 2) + (d3 * 3) + (d4 * 4) + (d5 * 5) + (d6 * 6) + (d7 * 7) + (d8 * 8) + (d9 * 9)
    return str(checkDigit % 11)

def calculate_isbn_checksum(isbn):
    tempN = 9
    checkNumber = 0
    while(isbn > 0):                            #basamaklarına ayırmaya ayarıyor.
        checkNumber += (isbn % 10) * tempN
        tempN -= 1
        isbn = int(isbn/10)
        
        
    return str(checkNumber % 11)
        
def is_isbn(isbn, checksum):
    tempIsbn = calculate_isbn_checksum(isbn)
    if(tempIsbn == str(checksum)):
        return True
    else:
        return False
    
    #return tempIsbn.equals(str(checksum))          #Bu şekilde de yazılabilir.

def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    if(box_h >= book_h):
        if(box_w >= book_w and box_d >= book_d):
            return True
        elif(box_w >= book_d and box_d >= book_w):
            return True
        else:
            return False
            
    else:
        return False
    
def get_smallest_box_for_book(book_w, book_d, book_h):
    #small(10,10,2)
    #medium(15,15,3)
    #large(20,20,4)
    if(book_w <= 10):
        if(book_d <= 10 and book_h <= 2):
            return 'Small'
        elif((book_d <= 15) and book_h <= 3):
            return 'Medium'
        elif((book_d <= 20) and book_h <= 4):
            return 'Large'
        else:
            return''
    elif(book_w > 10 and book_w <=15):
        if(book_d <= 15 and book_h <= 3):
            return 'Medium'
        elif(book_d <= 20 and book_h <= 4):
            return 'Large'
        else:
            return ''
    elif(book_w > 15 and book_w <=20):
        if(book_d <= 20 and book_h <= 4):
            return 'Large'
        else:
            return ''
    else:
        return ''
    
def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h): 
    count = 1
    if(book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h)):
        if(box_w > book_w):
            if((box_w / book_w)>1):
                count *= int(box_w / book_w)
        if(box_d > book_d):
            if((box_d / book_d)>1):
                count *= int(box_d / book_d)
        if(box_h > book_h):
            if((box_h / book_h)>1):
                count *= int(box_h / book_h)
            
        
    return count
    
def main():
    print("Welcome to the shipment calculation system.")
    print("1) Check ISBN")
    print("2) Check box/book size")
    print("3) Get smallest box size for book")
    print("4) Get num equally-sized books per box")
    
    inputM = input("Enter choice (1-4):")
    
    if(inputM == "1" or inputM == "2" or inputM == "3" or inputM == "4"):
        if(inputM == "1"):
            inputIsbn = int(input("Enter ISBN: "))
            inputCheck = int(input("Enter checksum: "))
            if(is_isbn(inputIsbn,inputCheck)):
                print("ISBN is valid (checksum did match).")
            else:
                print("ISBN is not valid (checksum did not match).")     
        elif(inputM == "2"):
            inputBoxW  = int(input("Enter box W: "))
            inputBoxD  = int(input("Enter box D: "))
            inputBoxH  = int(input("Enter box H: "))
            inputBookW = int(input("Enter book W: "))
            inputBookD = int(input("Enter book D: "))
            inputBookH = int(input("Enter book H: "))
            if(book_fits_in_box(inputBoxW, inputBoxD, inputBoxH, inputBookW, inputBookD, inputBookH)):
                print("The Book Fits In The Box")
            else:
                print("The Book Does Not Fit In The Box")
        elif(inputM == "3"):
            inputBookSizeW = int(input("Enter book W: "))
            inputBookSizeD = int(input("Enter book D: "))
            inputBookSizeH = int(input("Enter book H: "))
            temp = get_smallest_box_for_book(inputBookSizeW, inputBookSizeD, inputBookSizeH) == ''
            if(temp == '' ):
                print("This Size No Box")
            else:
                print("Box Size: "+temp)
        else:
            inputBxW  = int(input("Enter box W: "))
            inputBxD  = int(input("Enter box D: "))
            inputBxH  = int(input("Enter box H: "))
            inputBW = int(input("Enter book W: "))
            inputBD = int(input("Enter book D: "))
            inputBH = int(input("Enter book H: "))
            print("Number of books in the box:" + str(get_num_books_for_box(inputBxW, inputBxD, inputBxH, inputBW, inputBD, inputBH)))

    else:
        print("Sorry, that is not a valid option.")
    
    
main()   
