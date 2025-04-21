def main():
    while True:
        print("=== Simple Calculator ===")
        print("Select Operation: \n1. Addition \n2. Substraction \n3. Multiplication \n4. Division")
        select = int(input("Enter choice (1-4): "))
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        match select:
            case 1:
                print(f"{n1} +  {n2} = {n1 + n2}")
            case 2:
                print(f"{n1} - {n2} = {n1 - n2}")
            case 3:
                print(f"{n1} * {n2} = {n1 * n2}")
            case 4:
                if n2 != 0:
                    print(f"{n1} / {n2} = {n1/n2}")
                else:
                    print("second value cannot be zero")
            case default:
                print("please enter valid input")
        quest = input("Do you want to perform another calculation? (yes/no):")
        if quest == 'n' or quest == 'no': 
            break
        

if __name__ == "__main__":
    main()
