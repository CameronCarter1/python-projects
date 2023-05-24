def print_in_color(letter, color):
    text = ''
    if color == 'red':
        text = '\u001b[31m' + letter + '\u001b[0m'
    elif color == 'green':
        text = '\u001b[32m' + letter + '\u001b[0m'
    elif color == 'yellow':
        text = '\u001b[33m' + letter + '\u001b[0m'
    else:
        print("Color is not supported")
        return None
    print(text, end="")
    return text


def print_guess(secret_word, guess):
    required_letters = []
    for char in guess:
        if guess.find(char) == secret_word.find(char):
            print_in_color(char, "green")
            required_letters.append(char)
            continue
        elif char not in secret_word:
            print_in_color(char, "red")
            continue
        elif (char in secret_word) and (guess.find(char) != secret_word.find(char)):
            print_in_color(char, "yellow")
            required_letters.append(char)
            continue
        else:
            continue
    return required_letters


def get_guess(required_letters):
    guess = input("Enter your guess: \n")
    while is_valid_guess(guess, required_letters) == False:
        print("Your guess must contain all yellow and green letters from your previous guesses.")
        guess = input("Enter your guess: \n")
        continue
    if is_valid_guess(guess, required_letters) == True:
        return guess


def is_valid_guess(guess, required_letters):
    c = required_letters[:]
    for letter in required_letters:
        if letter in guess:
            c.remove(letter)
            continue
        else:
            break
    if c == []:
        return True
    else:
        return False


def is_game_over(secret_word, guess, tries_left):
    tries = 6
    if guess.upper() == secret_word.upper():
        print("Correct! You got it in", tries - tries_left, "tries!")
        return True
    elif tries_left == 0:
        print("Game over! The correct word is " + secret_word + ".")
        return True
    else:
        return False


secret_word = input("Enter the secret word: ")
required_letters = []
tries_left = 6
for i in range(tries_left):
    guess = get_guess(required_letters)
    if guess != secret_word and tries_left != 1:
        required_letters = (print_guess(secret_word, guess))
        tries_left = tries_left - 1
        is_game_over(secret_word, guess, tries_left)
    else:
        tries_left = tries_left - 1
        is_game_over(secret_word, guess, tries_left)
        break
