Correct = 0
vName = input("What is your name?\n\n")
print("Hello", vName, "!")
print("Welcome to my Quiz! This was created to test your general knowledge about a small variety of topics.")
print("--------------------------------------------------------------------------------------------------------")
quizList = ["1. Math", "2. Science", "3. History", "4. Geography", "5. Christmas!"]
print(quizList)
print("")
vQuiz = input("Please choose a quiz\n\n")
## Look into writing a way to confirm quiz choice
while vQuiz == "1":
    print("Welcome to the Simple Math Quiz. The following 5 questions will be based on a variety of math concepts")
    print("This math quiz simply requires a value for each question\n\n")
    print("Question 1: What is the square root of 144?\n\n")
    vM1 = input("Enter the correct answer\n\n")
    if vM1 == "12":
        print("Correct, on to the next question")
        break
    else:
        print("Incorrect, on to the next question")
        break
