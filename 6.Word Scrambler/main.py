import random

def main():
    print("Word Scrambler")
    while True:
        word = input("Enter a word to scramble (or 'quit'): ").strip()
        if word.lower() == 'quit':
            print("Goodbye!")
            break
        if len(word.split(' ')) == 1:
            #scrambled text and print the output 
            letters = list(word)
            random.shuffle(letters)
            print(f'Scrambled: {"".join(letters)}')
            
        

if __name__ == "__main__":
    main()
