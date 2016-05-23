'''
Pig Latin
'''
def pig_latin_word(word):
    '''
    Takes a word as a paramenter and translates it to pig latin.
    '''
    vowels = "aeiouAEIOU"
    i = 0
    const = []
    for char in word:
        if i == 0:
            if word[0] in vowels:
                return word+"way"
            while word[0] not in vowels:
                    i += 1
                    const.extend(word[0])
                    word = word[1:]
                    if word[0] in vowels:
                        return(word+''.join(const)+'ay')
                

                          
def pig_latin_sentence(eng_sentence):
    l = eng_sentence.split(" ")
    str(l)
    tran_sent = ""
    for word in l:
        if word in "!?.,'":
            word = word[:len(word)-1]
        tran_sent = tran_sent + pig_latin_word(word)
        tran_sent = tran_sent+ " "
    return tran_sent
def pig_latin_translator():
    print("-------------------------------") 
    print("English to Pig Latin Translator")
    print("-------------------------------")

    enter = str(input("\nEnter the English sentence: "))
    print("\nIn Pig Latin: " + pig_latin_sentence(enter))
    f = 'a'
    while f!= 'y' or 'n':
        f = input("Do another? [y/n] ")
        if f in "yY":
            pig_latin_translator()
        elif f in "nN":
            print("Goodbye!")
            break
        else:
            print("Please enter in a correct value")
            continue
