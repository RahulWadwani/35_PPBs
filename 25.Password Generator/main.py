import random 
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    password_characters = ""
    while len(password_characters) < length:
        choices = []
        if include_uppercase:
            choices.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if include_lowercase:
            choices.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
        if include_numbers:
            choices.append(random.choice("0123456789"))
        if include_special_chars:
            choices.append(random.choice("!@#$%"))
        
        if choices:  # Ensure there are valid options to choose from
            password_characters += random.choice(choices)

    return password_characters
def password_strength(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    if include_uppercase and include_lowercase and include_numbers and include_special_chars and len(password_length) >= 20:
        return "Very Strong"
    elif include_uppercase and include_lowercase and (include_numbers or include_special_chars) and len(password_length) >= 15:
        return "Strong"
    elif include_uppercase and include_lowercase and len(password_length) >= 12:
        return "Medium"
    elif include_uppercase or include_lowercase and len(password_length) >= 10:
        return "Weak"
    else:
        return "Very Weak"  

def main():
    create = True
    while create:
        print("==== Password Generator ====")
        print("Create super strong and secure passwords with ease!")
        len_pass = int(input("Enter password length (8-30):"))

        print("Let's customize your password.")
        inc1 = input("Include uppercase letters(A-Z)? (y/n)    : ")
        inc2 = input("Include lowercase letters(a-z)? (y/n)    : ")
        inc3 = input("Include numbers(0-9)? (y/n)              : ")
        inc4 = input("Include special characters(!@#$%)? (y/n) : ")

        print("Generating your magial password...")
        print("==== Your New Password ====")
        
        print(f"This can be your password : {generate_password(len_pass, inc1, inc2, inc3, inc4)}")
        print(f"Your password strength is : {password_strength(len_pass, inc1, inc2, inc3, inc4)}")

        print("==== Password Tips ====")
        print("Never use the same password for multiple accounts.")
        print("consider using a password manager to store your passwords securely.")
        print("change important passwords every few months.")
        print("Even strong passwords needs to be kept secret.")

        print("\n")
        again = input("Do you want to create another password? (y/n) : ")
        if again.startswith("N") or again.startswith("n"):
            create = False
            print("Thank you for using the password generator!")
            break

if __name__ == "__main__":
    main()
