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
'''
 +---+
[O   |
/|\  |
/ \  |
    ===''',
'''
 +---+
[O]  |
/|\  |
/ \  |
    ==='''
]


words   = {'Colors' : 'red orange yellow green blue indigo violet white black brown'.split(),
           'Shapes' : 'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
           'Fruits' : "apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato".split(),
           'Animals': "bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra".split()
        }



def get_random_word(words_dict):
    word_key    = random.choice(list(words_dict.keys()))
    choosen_word= random.choice(words_dict[word_key])

    return [choosen_word, word_key]

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

difficulty  = ''

while difficulty not in 'EMH':
    difficulty  = input().upper()
    
    if difficulty   == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    elif difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[6]
        del HANGMAN_PICS[5]

    

missed_letters  = ''
correct_letters = ''
secret_word, secret_set     = get_random_word(words)
game_is_done    = False

while True:
    print("The secret word is in the set: "+ secret_set)
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
            secret_word, secret_set     = get_random_word(words)
            game_is_done    = False
        else:
            break
    
