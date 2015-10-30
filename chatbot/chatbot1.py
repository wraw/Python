file = open("stop-words.txt")
stopwords = file.readlines()

def fWords(input):
    splitString = input.split(" ")
    
    fWords = [];
    
    for word in splitString:
        
        isStopWord = False
        for line in stopwords:
            stopWord = line.strip("\n");
            

            if word == stopWord:
                isStopWord = True
                break
        
        if isStopWord == False:
            fWords.append(word)
    

    return fWords

name = fWords(raw_input("Hello, What is your name? "))
color = fWords(raw_input("What is your favorite color? "))

print "Ah, so your name is %s, " \
"and your favorite color is %s." % (name, color)

feel = fWords(raw_input("Can you tell me how you feel today? "))

print "You are selfish stop talking about yourself" 

old = fWords(raw_input("How old are you? "))

if old < 18:
    print "You can't sit with us"
else:
    print "Okay cool"

hobby = fWords(raw_input("What you like to do? "))

print "That's cool! I like trains!!"

x = fWords(raw_input("Choose between black and white. "))

number = fWords(raw_input("What is your favourite number? "))

if number < 12:
    print "I don't like numbers more than 12"
else:
    print "I like you much"
    
    
    
    print "Goodbye" 
