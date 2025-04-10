
import random
#generate the word 
random_words = [
    "cactus", "orbit", "lantern", "velvet", "scribble",
    "meadow", "crunch", "spiral", "thunder", "breeze",
    "goblin", "pixel", "hammock", "jungle", "whisper",
    "eclipse", "marble", "anchor", "tumble", "snorkel"
]

# Hangman stages (0 to 6 lives)
hangman_stages = [
    '''
     ---------
     |     |
           |
           |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
           |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
     |     |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
    /|     |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
    /|\\    |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
    /|\\    |
    /      |
           |
           |
           |
     =========
    ''',
    '''
     ---------
     |     |
     O     |
    /|\\    |
    / \\    |
           |
           |
           |
     =========
    '''
]

random_index = random.choice(range(1,21))

random_word = random_words[random_index]
answer  = '_'*len(random_word) 

guessed_letters = set()

lives = 6

while '_' in answer and lives > 0:
    print(f"Current word: {answer}")
    print(f"Lives left: {lives}")
    print(hangman_stages[6 - lives])

    inputChar = input("Guess the character : ").lower()

    #ensure the user guesses only one character
    if len(inputChar) != 1 or not inputChar.isalpha():
        print("Please guess a single letter.")
        continue

    #If the letter has been already guessed then ask again
    if inputChar in guessed_letters:
        print("You have already guesses this letter.")
        continue

    #Add letter to guessed to set
    guessed_letters.add(inputChar)

    if inputChar not in random_word:
        lives -= 1

    #rebuild the new answer string based on the guess
    new_answer = ""
    for each_letter in random_word:
        if each_letter in guessed_letters:
            new_answer += each_letter
        else :
            new_answer += '_'
    answer = new_answer


# End of the game: Check win/lose
if '_' not in answer:
    print("Congratulations! You've guessed the word:", random_word)
else:
    print(hangman_stages[6 - lives])  # Show final hangman stage when user loses
    print("You lose! The word was:", random_word)