import random                          # random module import gareko (random word choose garna)
from words import words                # words.py file bata words list import gareko
import string                          # alphabet set banauna string module use gareko

# Valid word choose garne function
def get_valid_word(words):
    word = random.choice(words)        # words list bata random word liyeko
    while '-' in word or ' ' in word:  # yedi word ma dash ya space cha bhane
        word = random.choice(words)    # feri arko word choose garne
    return word.upper()                # word lai capital letter ma return garne

# Main game function
def hangman():
    word = get_valid_word(words)       # secret word choose gareko
    word_letters = set(word)           # guess garna baki letters haru set ma rakheko
    alphabet = set(string.ascii_uppercase)  # sabai capital alphabets ko set
    used_letters = set()               # user le guess gareka letters rakheko

    lives = 6                          # jati choti guess garna paunchha (6 lives)

    # Jaba samma guess baki cha ra lives khatam bhayeko chaina
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("You have used these letters: ", " ".join(sorted(used_letters)))

        # Word ko current status dekhaune (guessed letters dekhaune, aru '-')
        word_list = []
        for letter in word:
            if letter in used_letters:  # yedi guessed cha bhane
                word_list.append(letter)
            else:
                word_list.append('-')   # guess nagareko bhaye '-'

        print("Current Word: ", " ".join(word_list))

        # User bata guess input line
        user_letter = input("Guess a letter: ").upper()

        # Yedi valid letter ho ra paila guess nagareko ho
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # tyo letter guess list ma add garne

            if user_letter in word_letters:  # correct guess
                word_letters.remove(user_letter)
                print("Good guess!r")
            else:
                lives -= 1
                print("Letter is not in the word.")

        # Yedi already guessed letter ho
        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.")

        # Invalid character (jaasto number ya symbol)
        else:
            print("Invalid character. Please enter a valid letter.")

    # Game sakine bela je hunchha:
    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Function call garne
hangman()
