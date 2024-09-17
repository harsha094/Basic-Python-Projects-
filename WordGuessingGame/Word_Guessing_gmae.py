import random

name = input("What is your name?")
print("Welcome", name, "Good Luck 👍")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the characters")
#Initializing guess and turn 
guesses = ''
turns = 12
# main loop 
while turns > 0:
    #A counter for the number of characters that have not been correctly guessed.
    failed = 0
    # for loop to iterate through each characters
    for char in word:

        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
            
    if failed == 0:
             
            print("You Won", name)
            print("The word is: ", word)
            break
    print()
    #The user is prompted to guess a character.
    # The guessed character is added to the guesses string.
    guess = input("Guess the charcter:")
    guesses += guess
    # for incorrect guess 
    if guess not in word:
        turns -= 1
        print("Wrong Character!!!")
        print("You have", + turns, 'more guessess')
        #checking if a user has lost
        if turns == 0:
            print("You Loose", name)
            print("The word is: ", word)