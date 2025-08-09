from random_word import RandomWords

r = RandomWords()


def updating_index_of_guessed_word(guessed_letter, blanked_word, random_word_generated):
    updated_word = ""

    for i, letter in enumerate(random_word_generated):
        if letter == guessed_letter:
            updated_word += guessed_letter
        else:
            updated_word += blanked_word[i]  # keep previous character (underscore or guessed letter)

    print(f"Updated blank word now is: {updated_word}")
    return updated_word

 

def guess_the_word(blanked_word):
    print("Guessing the word")
    no_of_chances=5
    
    for chance in range(no_of_chances):
        
            print (f"This is your {chance+1}/{no_of_chances} chance to guess the word")
            guessed_letter = input("Please guess the letter: ").lower()
            print(f"You guessed letter is: {guessed_letter}")
            if(guessed_letter in random_word_generated):
                print("Your guessed letter is present in generated random word")
                blanked_word=updating_index_of_guessed_word(guessed_letter,blanked_word,random_word_generated)
                if "_" not in blanked_word:
                    print("You guessed the word! You win!")
                    break
            else:
                print("Sorry you guessed the wrong letter")
                
       
    else:
        print(f"You have exhausted your chances, The guessed word was : {random_word_generated}")
    
    
if __name__=="__main__":
    random_word_generated=""
    while True:
        word = r.get_random_word()
        random_word_generated=word
        if word and len(word) == 5:
            break


    print(f"Random word is: {random_word_generated}")

    blanked_word = "_" * len(random_word_generated)  
    print(f"Random word is: {blanked_word}") 

    guess_the_word(blanked_word)
