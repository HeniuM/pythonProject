import random

print('-------------------------------------------')
print('           GUESS THAT NUMBER GAME')
print('-------------------------------------------')

# scope of the guessing number
the_number = random.randint(0, 100)
# value that will never be true
guess = -1
name = input('Hello player, what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')

    # checking if putted number is not empty
    if guess_text.strip() == '':
        print('Please enter a number.')
        continue

    try:
        # conversion string to int
        guess = int(guess_text)
        # checking whether the number is in the given range
        if guess < 0 or guess > 100:
            print('Please enter a number between 0 and 100.')
            continue

    except ValueError:
        # error note when it's not an int
        print("Please enter a valid number.")
        continue

    # verification of the guessed number
    if guess < the_number:
        print('Sorry {}, your guess of {} was to LOW'.format(name, guess))
        print()
    elif guess > the_number:
        print('Sorry {}, your guess of {} was to HIGH'.format(name, guess))
        print()
    else:
        print('Congratulation {}, your guess of {} is correct number! '.format(name, guess))
        print('Well done! Try again guess the number :) ')

