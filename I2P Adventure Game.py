#This function is what we use to end the game. We call it everytime the user loses the game.
#This is askii art of game over. It is something we got from the internet.
def endgame():
    print("""

┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
""")
    print("All names have no resemblence to any living personnel.")
#This flat out ends the code
    quit()



#This list provided defines what is inside the backpack when it is called up
backpackList = ["sweaty gym clothes", "lunch", "wallet", "phone", "school books", "laptop"]
vhungerlevel = 0

#This records the users name
vName = input("What is your name?\n\n")

#This is a print section which is called up after the name input is answered
print("")
print("Why hello", vName, ", " "welcome to HKIS, the best school in Hong Kong! Although usually exciting, this year, school has taken a turn for the worse.")
print(vName,", " "you are a fearless, troublesome student, and have dreams of ditching class and running home.")
print("It is 9a.m, you are in Intro to Programming class and the teacher just left the class, a thought crosses your head.")

#This part provides the text for the question, which is then followed by an input which prompts the user for what they want to do
print("")
print("Should you:")
print("1. Leave class and run away")
print("2. Stay in class the whole day")
print("")
vInput = input("Choose what you want to do (write the number of the choice)\n\n")
print("")

#This part provides the text for the question where they input the wrong.
if vInput == "2":
    print("You're a loser.")
    print("Spending the whole day in Intro to Programming class, you die of boredom")
    print("Also, Dr. Rungee comes in and fines the whole class $28,000 USD")
    print(endgame())
    quit()

#This provides the text for the question when the input the correct answer.
elif vInput == "1":
    vhungerlevel = vhungerlevel + 5
    print(vhungerlevel)
    print("You're a pretty cool person")
    print("You grab your backpack; look inside, then run out of the classroom with it in your hand.")
    print("Inside, you find", backpackList)
    print("Thinking about how to leave, you wonder which exit you should take to leave the school.\n\n")

#This tells that if the user selects a number that is not '1' or '2', then the code will give a short message then end
elif vInput != "1" or "2":
    print("Wow! Funny guy! Please follow the rules.")
    quit()


#This is just a simple input --> Print question answer correctly code
print("Should you:")
print("1. Go through the High School")
print("2. Go through the Middle School back door")
vexit = input("Which exit would you like to choose? \n\n")

#This shows what happens when you choose the wrong answer, which ends the game, hence the 'quit()'
if vexit == "1":
    print ("Oh no! As you are leaving, the guards stop and take you to Alan Runge, he fines you $28,000...")
    print(endgame())
    quit()

#This shows what happens when you choose the correct answer, and intoduces a hunger level which is important to the story line
elif vexit == "2":
    print ("Nice! You chose the correct route\n\n ")
    vhungerlevel = vhungerlevel + 5
    print ("Your hunger level is now", vhungerlevel, "/10")

print ("Watch out, your hunger level is now",vhungerlevel,"/10. Should you go into the Middle school cafeteria to eat? Or look into your backpack?")

print("Should you:")
print("1. Go to the Cafeteria and buy lunch")
print("2. Look in your backpack")

vhungry = input("Where do you want to eat lunch? \n\n")

if vhungry == "1":
    print ("Well, you run into Alan Runge at the cafeteria, get fined $28,000 USD")
    print(endgame())
    quit()

#Here, we summon the list that we provided at the top, which is essential to the storyline
elif vhungry == "2":
    print ("You chose wisely")
    print("You find lunch, and you eat it")
    vhungerlevel = vhungerlevel - 10
    print("Your hunger level is now 0/10")
    backpackList = ["Sweaty Gym Clothes", "Wallet", "Phone", "School Books", "Laptop"]
    print ("Now you have", (backpackList), "in your backpack\n")

print("Now you have to figure out how to leave the South Side and go home")
print("Do you want to:")
print("1: Go through the country park")
print("2: Wait for the bus to central")
vescape = input("How to you want to escape\n \n")

if vescape == "1":
    print("Okay, now you have to cross the road. You start the cross the road when you hear a loud honk from your right!")
    print("You forgot to check whether there were any cars coming!")
    print("You get hit by a car! Its Dr. Alan Rungee!")
    print("You are caught for leaving school, fined $28,000 USD and now you have a broken back!")
    print(endgame())
    quit()

elif vescape == "2":
    print("Great! You chose wisely")
    print("You wait for the bus. It arrives. You get on.")

print ("You can either sit on the: ")
print ("1: Top Deck")
print ("2: Bottom Deck")
vdeck = input("Where do you want to sit?\n\n")

if vdeck == "2":
    print("Oh dear! Mr. Rungee got on at the next stop!")
    print("You get caught and fined $28,000 USD")
    print(endgame())
    quit()

elif vdeck == "1":
    print ("You chose wisely")

print("Oh look! Stanley is coming up! Do you want to get off at Stanley?")
print("1: Get off at Stanely")
print("2: Take the bus to Central")
vStan = input("What do you want to do?\n\n")

if  vStan == "1":
    print("Oh no! As you get off so does Mr. Rungee! You get caught and fined $28,000 USD")
    print(endgame())
    quit()

elif vStan == "2":
 print("You chose well")

print ("Now you have to home. Wait! There is something vibrating in your bag!")
print (backpackList)
print ("Oh. Someone (No caller ID) is calling you!")
print("""Should you"
1: Pick it up
2: Let it ring""")
vring = input("What do you want to do?\n\n")


if vring == "2":
    print("""Woah, someone is tapping you on the back. It's Dr. Rungee!
You get fined $28,000 USD!""")
    print(endgame())
    quit()

if vring == "1":
    print("Oh No! It's Dr. Rungee")

print("""What do you want to do?
1: Throw your phone away
2: Answer it""")
vcall = input("What will you do?\n\n")

if vcall == "2":
    print("""You do not deserve to play this game  \n \n """)
    quit()

elif vcall == "1":
    print("You chose well.")

print ("Oops! Your throw hit someone")
print("""Should you:
1: Go help them
2: Get home as soon as possible""")
vthrow = input("What will you do?\n\n")

if vthrow == "1":
    print("""It's Dr. Rungee! You get fined $28,000 USD!""")
    print(endgame())
    quit()

elif vthrow == "2":
    print("You chose well. ")

print("""Now what do you want to do?
1: Go home
2: Go to the train station""")
vend1 = input("What will you do?\n\n")

if vend1 == "2":
    print("Congratulations! You have safely reached the train station. But wait....")
    print("Continued next time, with more time given!")
    print("Note: Names are fictitious and have no resemblance to any living personnel")

    quit()

if vend1 == "1":
    print("You chose well")

print("""Do you want to:
1; Take your stuff and leave immediately?
2: Spend the night?""")
vend2 = input("What will you do?\n\n")

if vend2 == "2":
    print("*Spends the night*")
    print("""The next morning:
    You hear the doorbell ring. You go to open it.
    It's Dr. Rungee!! You are caught and fined $28,000 USD""")
    print(endgame())
    quit()
#This is the end of the code, you are provided with a congratulations menu, then the code closes.
if vend2 == "1":
    print("Congratulations! You have safely reached the train station. But wait....")
    print("Continued next time, with more time given!")
    print("Note: Names are fictitious and have no resemblance to any living personnel")
wing



