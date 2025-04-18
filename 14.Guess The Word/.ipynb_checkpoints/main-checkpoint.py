import random

def main():
    print("=== WORD SCRAMBLE GAME ===")
    words = ["python","coding","game","computer","fun","learn"]
    while True:
        org_word  = random.choice(words)
        letters = list(org_word)
        random.shuffle(letters)
        scrambled = "".join(letters)
        print(f"Scrambled word: {scrambled}")
        guess = input("What's the word: ")
        if guess == org_word:
            print("Correct! You Win!")
        else:
            print(f"The correct word was: {org_word}")
            
        pa = input("Play Again? (yes/no): ")
        if pa == 'no' or pa == 'n':
            print("Thanks for playing!  ")
            break

if __name__ == "__main__":
    main()
