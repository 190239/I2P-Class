import random

guessTaken = 0
print('Hello! What is your name?\n')
myName = input()
number = random.randint(1, 20)
print("\n\nHowdy " + myName + "! Please choose a number between 1 and 20")

while guessTaken < 100:
    guess = int(input('Take a guess.\n \n'))
    guessTaken = guessTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        print ("Congratulations, You win!!", "You guessed the number in ", guessTaken, "guesses.")
