import random

# ask user for a number in order to establish a range of numbers
range_for_guesses = input("Enter a number: ")

# check to see if the user input is a number and if it is, convert it to an integer
if range_for_guesses.isdigit():
    range_for_guesses = int(range_for_guesses)

    # check to see if range number is larger than 0
    if range_for_guesses <= 0:
        print("Please enter a number larger than 0 next time :).")
        quit()
else:
    print("Please enter a number this time :).")
    quit()

random_number = random.randint(0, range_for_guesses)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print("Please enter a number larger than 0 next time :).")
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_number:
        print("That's correct! Well Done!")
        break
    else:
        if user_guess > random_number:
            print("Too high, try again!")
        else:
            print("Too low, try again!")

print("You got it in", guesses, "guesses!")
