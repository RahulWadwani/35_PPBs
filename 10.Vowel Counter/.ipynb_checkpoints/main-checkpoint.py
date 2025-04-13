def main():
    print("Vowels Counter")
    vowels = ['a','e','i','o','u']
    while True:
        sentence = input("Enter some text (or 'quit'):")
        counter = 0
        if  sentence.lower() == 'quit':
            break
        for letters in sentence.lower():
            if letters in vowels:
                counter  += 1
        print(f"That text has {counter} vowels!")
            

if __name__ == "__main__":
    main()
