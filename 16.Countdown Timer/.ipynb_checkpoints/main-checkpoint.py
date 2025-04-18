import time 

def main():
    print("=== COUNTDOWN TIMER ===")
    print("Count down from your chosen seconds!")
    while True:
        timeis = int(input("Enter seconds to coundown from: "))
        for i in range(timeis,0,-1):
            print(f"{i} seconds remaining ...")
            time.sleep(1)
        print("Countdown complete!")
        user = input("Start another countdown? (yes/no): ")
        if user == 'no' or user == 'n':
            print("Thanks for using the countdown timer!")
            break
    
        

if __name__ == "__main__":
    main()
