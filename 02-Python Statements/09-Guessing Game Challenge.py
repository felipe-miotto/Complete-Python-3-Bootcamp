import random
num = random.randint(1, 100)

print("This is a guessing number game!")
print("I'm thinking of a number between 1 and 100!")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:

    guess = int(input('My secret number is between 1 and 100.\n Your guess is: '))

    if guess > 100 or guess < 1:
        print('OUT OF BOUNDS. Please try again: ')
        continue

    if guess == num:
        print(f'Congratulations! You won!! You got it right after only {len(guesses)} tries!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
