#Continue to build this, Paul.
#It's worth your time to invest in yourself.

#Smart-ass Program

#the function of the program


def answerBank ():
    if userAsk <= 15:
        print("\nWhat is wrong with you?\nI can not believe you asked me that.\n___________________\n")
    elif userAsk >= 16 and userAsk <= 25:
        if userAsk >= 19 and userAsk <= 22:
            print("HA, Dumb Ass!\n___________________\n")
        if userAsk >= 23 and userAsk <= 24:
            print("OMG!\nHow senseless can one person be?\n ______________________\n")
        print("\nIs that really your question!?\nWOW!\nThe answer is, you are an idiot.\n_____________\n")
    elif userAsk >= 26 and userAsk <= 35:
        if userAsk >= 28 and userAsk <=33:
            print("Today is your lucky day.\nBut it's still going to SUCK!\n____________________\n")
        if userAsk >=34 and userAsk <= 35:
            print("GUMP!\nYou're a Goddamn genius!\n__________________\n")
        print("\nWho cares?\nThe world is ending and you ask that.\n_____________\n")
    elif userAsk >= 36 and userAsk <=45:
        if userAsk >= 38 and userAsk <=42:
            print("Well, WOOP PA DOOPITY DOO!\n_______________________\n") 
        print("\nAnything else, your highness??\nYou had one question and that is the best you could do?\n______________________\n")
    elif userAsk >45:
        print("\nCalm down, Karen.\nI am the manager.\n=======================\n")
        
#import functionality
#from Answers import answerBank

    #chose to not use loop as it is ask only one query
    #start of program loop    
#while True:    

    #Title to show at prompt and display warning to user.
print("\nAll answers found here.\nAsk anything, BUT...\nyou can only ask one question.\n")

    #The prompt 
    #userAsk = input("Enter your question. ")
userAsk = len(input("Enter you question. "))

#import the function
#
# from test import answerBank

    #give me feedback here during DNR
print(userAsk)

#Call the function
answerBank()

