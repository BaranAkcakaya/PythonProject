CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

def is_valid_consonant(isConsonants):
    if(len(isConsonants) > 1):
        return False
    else:
        for tempCons in CONSONANTS:
            if(tempCons == isConsonants.lower()):
                return True
        else:
            return False

def is_valid_vowel(isVowels):
    if(len(isVowels) > 1):
        return False
    else:
        for tempVowel in VOWELS:
            if(tempVowel == isVowels.lower()):
                return True
        else:
            for tempVowel in VOWELS_WITH_ACCENT:
                if(tempVowel == isVowels.lower()):
                    return True
            else:
                return False

def is_valid_single_word(isWord):
    for tempCharacter in isWord.lower():
        if(tempCharacter in PUNCTUATION):
            return False
        else:
            if(tempCharacter in CONSONANTS):
                continue
            elif(tempCharacter in VOWELS):
                continue
            elif(tempCharacter in VOWELS_WITH_ACCENT):
                continue
            else:
                return False
    return True

def is_valid_phrase(isPhrase):
    for tempCharacter in isPhrase.lower():
        if(tempCharacter in CONSONANTS):
            continue
        elif(tempCharacter in VOWELS):
            continue
        elif(tempCharacter in VOWELS_WITH_ACCENT):
            continue
        elif(tempCharacter in PUNCTUATION):
            continue
        elif(tempCharacter == ' '):
            continue
        else:
            return False
    return True

def  get_consonant_pronunciation(getConsonant):
    if(is_valid_consonant(getConsonant) == False):
        return ""
    else:
        if(getConsonant.lower() == 'j'):
            return 'GE'
        else:
            return getConsonant.upper()

def get_vowel_pronunciation(getVowel):
    if(is_valid_vowel(getVowel) == False):
        return ""
    else:
        if(getVowel.lower() == "a" or getVowel.lower() == "à"):
            return "A"
        elif(getVowel.lower() == "e" or getVowel.lower() == "è"):
            return "E"
        elif(getVowel.lower() == "ì"):
            return "EE"
        elif(getVowel.lower() == "ò"):
            return "O"
        elif(getVowel.lower() == "o"):
            return "U"
        else:
            return getVowel.upper()

def get_diphthong_pronunciation(getDiphthong):
    if(getDiphthong.lower() in DIPHTHONGS):
        if(getDiphthong.lower() == 'aw'):
            return 'OW'
        elif(getDiphthong.lower() == 'ay'):
            return 'EYE'
        elif(getDiphthong.lower() == 'ew'):
            return 'AO'
        elif(getDiphthong.lower() == 'ey'):
            return 'AY'
        elif(getDiphthong.lower() == 'iw'):
            return 'EW'
        elif(getDiphthong.lower() == 'ow'):
            return 'OW'
    else:
        return ""

def get_word_pronunciation(getWord):
    newString = ''
    j = 0
    for i in range(0,len(getWord)):
        if(j <= i):
            if(getWord[i:i+2].lower() in DIPHTHONGS):
                newString = newString + get_diphthong_pronunciation(getWord[i:i+2].lower())
                j = i + 2
            elif(getWord[i:i+2].lower() == 'dj'):
                newString = newString + 'J'
                j = i + 2
            elif(is_valid_vowel(getWord[i].lower())):
                newString = newString + get_vowel_pronunciation(getWord[i].lower())
            elif( is_valid_consonant(getWord[i].lower())):
                newString = newString + get_consonant_pronunciation(getWord[i].lower())
            else:
                newString = ""
                break
    return newString.upper()

def tokenize_sentence(getTokenize):
    temp = 0
    listSent = []
    for j in range(0, len(getTokenize)):
        if(j >= temp):
            if(getTokenize[j] in PUNCTUATION or getTokenize[j] == " "):
                listSent.append(getTokenize[temp:j])
                listSent.append(getTokenize[j])
                temp = j + 1
    listSent.append( getTokenize[temp:])
    temp = j
        
    for tempSent in listSent:
        if(tempSent != ''):
            if(is_valid_phrase(tempSent) == False):
                return []
        else:
            listSent.remove(tempSent)
    return listSent
        
def get_sentence_pronunciation(getSentence):
    newS = ""
    if(tokenize_sentence(getSentence) == []):
        return ""
    else:
        for tempSent in tokenize_sentence(getSentence):
            if(tempSent in PUNCTUATION or tempSent == ' '):
                newS = newS + tempSent
            else:
                newS = newS + get_word_pronunciation(tempSent)
        
        return newS
print( get_sentence_pronunciation('Andi ejayan?'))
        