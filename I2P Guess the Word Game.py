import random

tries = 0

print("Guess one of the following words: Island, Empty, Cool, Awesome, Fun")

##Here I created a list of words which the code will randomly pick from
##The last part of this converts the word into lowercase which allows the player to write the word in lowercase

WORDS = ("Island", "Empty", "Cool", "Awesome", "Fun")
word = random.choice(WORDS)
word = word.lower()

##The first part of this explains the variable of correct being the word given
##This section of the code tells the player how many letters the randomly generated word has

correct = word
length = len(word)
length = str(length)

##This part of the code is what tells the player how long the word is depending on the randomly generated word

guessTaken = 0

guess = input("The word is " + length + " letters long. Guess a letter!: ")


##This sets the conditions for the answer that is provided by the player

if guess == correct:
    print("Congrats! You are smart!")
    print("It took you", guessTaken, "guesses to get it right!")
if guess != correct:
    print("Incorrect!")
    guessTaken = guessTaken + 1

##In case they somehow get it wrong, this part of the code makes it so that the player can try again

while guess != word:
    guess = input('Try Again.\n \n')
    guessTaken = guessTaken + 1
if guess == word:
    print("Good Job! You were correct :)")
    print("It took you", guessTaken, "guesses to get it right!")


