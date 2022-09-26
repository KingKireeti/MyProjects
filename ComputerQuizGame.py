print("Welcome to my Game!")

player = input("Do you want to play? ")
if player != "yes" :
        quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU Stand for? ")
if answer == "central processing unit":
    print("Yes! Correct")
    score += 1
else:
    print("Oops! Wrong Answer")

answer = input("What does GPU Stand for? ")
if answer == "graphics processing unit":
    print("Yes! Correct")
    score += 1
else:
    print("Woops!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Yes! Correct")
    score += 1
else:
    print("Woops wrong answer")

answer = input("What does PSU stand for? ")
if answer  == "power supply unit":
    print("Yes! Correct")
    score += 1
else:
    print("woops wrong answer good try ")

print("You got " + str(score) + " Quesiton(s) correct")
print("You got " + str(score/ 4 * 100) + "% of the questions correct. Good Job!")



