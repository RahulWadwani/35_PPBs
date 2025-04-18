"""
main.py - Starter script
"""
import random 
def main():
    print("Welcome to the number Guessing Game!")
    print("I'm Thinking of a number Between 1 and 100. you have 10 attempts.")
    org = random.randint(1,100)
    count = 1
    while count != 10:
        guessed = int(input(f"Attempt {count}/10. Enter you guess:"))
        if guessed ==  org:
            print(f"Congratulations! you have guessed the number {guessed} in {count} attempts")
            break
        elif guessed > org:
            print("Too high! Try a lower number!")
        else:
            print("Too Low! Try a higher number!")
        print(f"you have {10-count} attempts left")
        count += 1 

if __name__ == "__main__":
    main()
