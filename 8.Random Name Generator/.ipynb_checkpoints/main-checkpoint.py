import random 

def main():
    print("Fanatsy Name Generator")
    first_parts = ["sky","star","Moon","Sun","Fire","Ice"]
    last_parts = ['rider','walker','hunter','seeker','dancer','keeper','singer']
    count = int(input("How many names do you want? "))
    for i in range(count):
        first = random.choice(first_parts)
        last = random.choice(last_parts)
        print(f'{first}{last}')

if __name__ == "__main__":
    main()
