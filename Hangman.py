import random

HANGMAN_PICS    = [
'''
+---+
    |
    |
    |
   ===''',
'''
+---+
O   |
    |
    |
   ===''',
'''
+---+
O   |
|   |
    |
   ===''',
'''
 +---+
 O   |
/|   |
     |
    ===''',
'''
 +---+
 O   |
/|\  |
     |
    ===''',
'''
 +---+
 O   |
/|\  |
/    |
    ===''',
'''
 +---+
 O   |
/|\  |
/ \  |
    ===''',
]


words   = """ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra""".split()

def get_random_word(words_list):
    random_index    = random.randint(0, len(words_list)-1)

    return words_list[random_index]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print("Missed Letters : ", end=' ')
    for letter in missed_letters:
        print(letter,end='')
    print()

    blanks  = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks  = blanks[:i] + secret_word[i] + blanks[i+1:]
        
    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):

    while True:
        print("Guess A Letter : ")
        guess   = input()
        guess   = guess.lower()

        if len(guess) != 1:
            print("Please Enter Single Char...")
        elif guess in already_guessed:
            print("You Already Choosed This Letter, Plz Choose Another One")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please Enter A letter")
        else:
            return guess

def play_again():
    print("Do You Wanna Play Again ?...")
    return input().lower().startswith('y')

print("H A N G M A N")
missed_letters  = ''
correct_letters = ''
secret_word     = get_random_word(words)
game_is_done    = False

while True:
    
    display_board(missed_letters, correct_letters, secret_word)

    guess   = get_guess(missed_letters+correct_letters)


    if guess in secret_word:
        correct_letters += guess

        found_all_letters   = True

        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters   = False
                break
        if found_all_letters:
            print("Yes! The Secret Word Is '" + secret_word + "'! You Have Won")
            game_is_done    = True
    else:
        missed_letters  += guess
        if len(missed_letters) == len(HANGMAN_PICS)-1:
            print("'You have run out of guesses!\nAfter " + str(len(missed_letters))+ " Missed Guesses  And " + str(len(correct_letters)) + " Correct Guesses, The Word Was '" + secret_word + "'")
            game_is_done    = True
    
    if game_is_done:
        if play_again():
            missed_letters  = ''
            correct_letters = ''
            secret_word     = get_random_word(words)
            game_is_done    = False
        else:
            break
    
