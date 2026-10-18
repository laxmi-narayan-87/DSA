# PYPROJPR03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Comparing the guess

We have now generated the random number.

Let us incorporate the algorithm or the judge which evaluates and gives us clues.

- The 'Secret number' and user guessed number are compared with the following result If the user guess is greater than or less than 'Secret number' by 10 - the system output is 'Cold' If the user guess is + / - 10 from the 'Secret number' - the system output is 'Hot' If the user guess matches the 'Secret number' - the system prompts 'You guessed it right!!'
### Task

Update the if / elif / else conditions in the IDE to meet the conditions defined above

 **Note:**  We are just writing the logical conditions here.
There is one last step remaining.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T17:44:42.186Z  

```cpp
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
```

---

[View on CodeChef](https://www.codechef.com/problems/PYPROJPR03)