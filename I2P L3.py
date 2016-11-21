##if else
vScore = 75
if vScore >= 50:
    print("You have Passed!")
else:
    print("You have FAILED")

##if in

vMonth = "September"
vLetter = "e"

if vLetter in vMonth:
    print("There is a letter", vLetter, "in", vMonth)
else:
    print("There is NOT a letter",vLetter, "in", vMonth)

##Next things
vChoice = input("Enter Number 1 to 3: ")
print()

if vChoice == "1":
    print("Chosen Item 1. Good Job")

elif vChoice == "2":
    print("Chosen Item 2")

elif vChoice == "3":
    print("Chosen Item 3")

else:
    print("Sorry, but", vChoice, "isn't a valid answer.")

input("/n/nPress the enter key to exit.")

# program that works out the score for a given word
# a = 5
# e = 4
# i = 3
# o = 2
# u = 1

vWord = input("Enter a word: ")

# Convert the word into lower case
vWord = vWord.lower()

# Set score to be 0
score = 0

# Create a loop so that
# letters are looked at one by one...
for letter in vWord:
    if letter == "a":
        score = score + 5
        print(letter, "is worth 5 points!")
        print("You have", score, "points!")
    elif letter == "e":
        score = score + 4
        print(letter, "is worth 4 points!")
        print("You have", score, "points!")
    elif letter == "i":
        score = score + 3
        print(letter, "is worth 3 points!")
        print("You have", score, "points!")
    elif letter == "e":
        score = score + 2
        print(letter, "is worth 2 points!")
        print("You have", score, "points!")
    elif letter == "u":
        score = score + 1
        print(letter, "is worth 1 points!")
        print("You have", score, "points!")
    #if someone puts something other than a vowel
    else:
        print(letter, " is worth 0 points :/")
        print("You have", score, "points!")
    #End of loop
    #Print the score

print("Total score is ", score )
