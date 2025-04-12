def callCase(text,value):
    match value:
        case 1:
            print(text.upper())
        case 2:
            print(text.lower())
        case 3:
            print(text.title())
        case 4: 
            print(text.capitalize())
        case _: 
            print("Invalid choice.")
    
def main(text):
    print("Kindly select the appropriate options: \n1. Upper Case \n2. Lower Case \n3. Title Case \n4. Sentence Case")
    val = int(input("Enter the value: "))
    callCase(text,val)


if __name__ == "__main__":
    txt = input("Enter some text: ")
    main(txt)
