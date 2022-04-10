import random
# Extract a random word from my text file

# This method reads all the words in the game from a file and randomly picks a word
def word_selected(fname):
    word_file = open(fname,'r+')
    secret_word = random.choice(word_file.read().split())
    word_file.close()
    return secret_word

secret_word = word_selected('hangman.txt')

# Display randomly chosen word in dash:
def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(secret_word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)

word_selected_dashed = word_selected_dashed()
print(word_selected_dashed)

guesses = 7

guessed_word = list(word_selected_dashed)

while guesses > 0:
    if ''.join(guessed_word) == secret_word:
        print("Congratulations, winner winner shrimp dinner")
        break

    print('you have got '+ str(guesses)+ ' wrong tries ')
    user_guessed_letter = input('Guess a letter >>>>> \n')


    if user_guessed_letter in secret_word:
        print('Correcto Mr. Bolobo!')
        for i in range(len(secret_word)):
            if list(secret_word)[i] == user_guessed_letter:
                guessed_word[i] = user_guessed_letter
        print(''.join(guessed_word))

    elif user_guessed_letter not in secret_word:
        print('GGs wrong!')
        guesses -= 1
       
if guesses == 0 :
    print('you thought, you have ran out of guesses')
