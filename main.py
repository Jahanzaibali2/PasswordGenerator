import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result = ""

for i in range (1, nr_letters + 1):
    let = random.choice(letters)
    result += let

for i in range (1, nr_numbers + 1):
    let = random.choice(numbers)
    result += let

for i in range (1, nr_symbols + 1):
    let = random.choice(symbols)
    result += let

x = ''.join(random.sample(result,len(result)))
print(x)




import random

def display_intro():
    print("Welcome to the Word Guessing Game!")
    print("You have to guess the word selected by the computer.")
    print("You can guess one letter at a time or try to guess the whole word.")
    print("You have a limited number of attempts. Good luck!\n")

def get_word():
    words = ["python", "javascript", "java", "kotlin", "swift", "golang", "ruby", "perl", "haskell", "rust"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_player_input(guessed_letters):
    while True:
        guess = input("Enter a letter or guess the word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            else:
                return guess
        elif len(guess) == len(word):
            return guess
        else:
            print("Invalid input. Please enter a single letter or try to guess the word.")

def main():
    display_intro()
    word = get_word()
    guessed_letters = set()
    attempts = 10

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        print(f"Word: {display_word(word, guessed_letters)}")

        guess = get_player_input(guessed_letters)

        if len(guess) == 1:
            guessed_letters.add(guess)
            if guess in word:
                print(f"Good guess! The letter '{guess}' is in the word.")
            else:
                attempts -= 1
                print(f"Sorry, the letter '{guess}' is not in the word.")
        else:
            if guess == word:
                print(f"\nCongratulations! You guessed the word '{word}' correctly!")
                break
            else:
                attempts -= 1
                print(f"Wrong guess. The word is not '{guess}'.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed all the letters in the word '{word}'!")
            break

    if attempts == 0:
        print(f"\nGame Over! The correct word was '{word}'.")

if __name__ == "__main__":
    main()
