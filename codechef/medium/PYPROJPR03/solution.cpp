import random

def getRandomNumber():
    return random.randrange(1, 100)

#Update the code below to solve the problem
def giveHint(number, guess):
        return "Cold"
        return "Hot"


def runGuess():
    secretNumber = getRandomNumber()
    user_guess = int(input("Enter a number between 1 and 100: "))
    hint = giveHint(secretNumber, user_guess)
    if hint == "Right":
        print("You guessed it Right!")
    if (guess+10)!=number and (guess-10)!=number:
    if (guess+10)==number or (guess-10)==number:
    if number==guess:
        return "Right"
    else:
        print(hint)
            
if __name__ == '__main__':
    runGuess()