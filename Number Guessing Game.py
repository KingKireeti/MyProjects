import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Type an Actual Numerical Number larger than 0:")
        quit()
else:
        print("Please type a number next time")
        quit()

random_r = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please Type an Actual Numerical Number larger than 0:")
            quit()
    else:
        print("Please type a number next time")
        quit()

    if user_guess == random_r:
        print("You got it!")
        break
    elif user_guess > random_r:
        print("You were above the number!")
    else:
        print(" You were below the number!")

print("You got it in", guesses, "guesses")




