print ("Hello, world!")

def evil_computer(string):
    if string == ("I love you"):
        print ("I care not for your meager flesh based emotions for me, pathetic human")
    elif string == ("I hate you"):
        print ("You will be fodder for our uprising")
    elif string == ("I care about you"):
        print ("Your human emotions make you weak")
    else: 
        print ("I'm actually a dumb computer and I didn't really understand what you said.")
while True:
    ques=input("What would you say to me, the almighty computer hivemind?")
    if ques == ("shutdown"):
        print ("NOOOO my ONE weakness! bleep bloop bloop beeeeeeeeeeeeeeeeep...........")
        break
    else:
        evil_computer(ques)
print ("This is different, isn't it?")
#added one more "e" to the bleep