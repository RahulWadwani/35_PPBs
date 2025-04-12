def main(ch):
    if len(ch) == 1:
        if (ord(ch) in range(97,123)) or (ord(ch) in range(65,91)):
            print("Given charachter is an alphabet.")
        elif (ord(ch) in range(48,58)):
            print("Given character is an number.")
        else:
            print("Given character is a special charachter.")
    else:
        print("Only character's are acceptable. Kindly input a character with length as 1.")

if __name__ == "__main__":
    char = input("Enter the charachter value: ")
    main(char)
