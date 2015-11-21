#make a class with functions that compare two strings,
# if its the same, increase score
# if its not the same, do nothing

# show a word, phrase, sentence on screen
# user will try to pronounce the on screen text
# api will convert user's audio input into text
# we will compare the user text to original text
#increment score as needed
# increase difficulty level if user is continuously successful
# decres difficulty level if user is continuosly unsuccessful



class GameFunctions:
    def __init__(self, myText = "", myScore = 0):
        #the text to display on screen
        self._text = myText
        self._score = myScore
        self._scoreIncrement = 1 #the score will increse by this much each time the user gets the answer correct

    #yourText is the user's input
    def isCorrect(self, yourText = ""):
        return (self._text == yourText)

    def incScore(self):
        self._score += self._scoreIncrement

    #create a  function to query an online database of words to setText to a random word

    #getters
    def getScore(self):
        return self._score

    def getText(self):
        return self._text

    #setters
    def setScore(self, num = 0):
        self._score = num

    def setText(self, myText = ""):
        self._text = myText


# this is the main function for ParrotMe

myText = "Raymond"
ParrotMe = GameFunctions()
while True:
    #myText = randomWordFromTheDictionary
    ParrotMe.setText(myText)

    #get user's audio input
    yourText = input("Enter your text: ")   #use api to convert user audio into text

    if yourText == "": #to quit the game
        break

    if ParrotMe.isCorrect(yourText):
        ParrotMe.incScore()
        print(ParrotMe.getScore())

#this is the main function for SpellingBee
    #program will play an audio file of a word
    #api will convert that audio file into text
    #user will input the spelling of that word on the keyboard
    #program will

myText = "Kevin"
#select a word (text format from some database of words)
#use api to convert to an audio file
#play the audio file
SpellingBee = GameFunctions()    #pass in the text (converted from the audio file)

while True:
    #select a word (text format from some database of words)
    SpellingBee.setText(myText)
    #use api to convert to an audio file
    #there is a button here that the user can press to play the audio file

    yourText = input("Enter your text: ")

    if yourText == "":  #to quit the game
        break

    if SpellingBee.isCorrect(yourText):
        SpellingBee.incScore()
        print(SpellingBee.getScore())

