# Asking the user's name and if they want to take the quiz

Your_Name = input("What is your name?: ")
Your_Name = Your_Name.capitalize()
player = input("\n" "Hello " + Your_Name.capitalize() + ", " + " Are you ready to take the quiz?: ")
if player == 'yes':
    player = input("\n" "Are you sure?: ")
if player == 'yes':
    print("\n" "Alright " + ", " " GoodLuck :) " )
else:
    print("\n" "Okay Thanks " + Your_Name.capitalize())
    quit()

# The Game start now 
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT! " + "GREAT JOB! ")
        return 1
    else:
        print("WRONG! " + "BETTER LUCK NEXT TIME! ")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")

    if response == "yes":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "What does GPU stand for?: ": "A",
 "What does RAM stand for?: ": "D"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. Graphics Processing Unit","B. Graphics Process Unit", "C. GPU", "D. None of the Choices"],
          ["A. RAM", "B. Random Accessible Memory", "C. What's RAM?", "D. Random Access Memory"]]

new_game()

while play_again():
    new_game()

print("\n" "Alright, Thanks for taking the quiz")

# -------------------------