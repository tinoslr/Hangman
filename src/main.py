import random

# List of words
word_list = ["python", "lasagna","japan","witcher"]
# randomly choosen word, which should be guessed
secret_word = random.choice(word_list)

# track guesses and failed guesses
correct_guesses = set()
incorrect_guesses = set()
left_attempts = 6


def display_game_state():
    display_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word:{display_word}")
    print(f"Incorrect Guesses: {" ".join(incorrect_guesses)}")


while True:
    display_game_state()
    guess = input("Enter your guess: ").lower()

    if guess in secret_word:
        correct_guesses.add(guess)

        #Check for win
        if set(secret_word).issubset(correct_guesses):
            print("You have Won")
            break
    
    else:
        incorrect_guesses.add(guess)
        left_attempts -= 1

        #check for loosing condition
        if left_attempts == 0:
            print("Game Over")
            print(f"The secret word was: {secret_word}")
            break