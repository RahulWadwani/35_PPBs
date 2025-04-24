"""
main.py - Starter script
"""
import random 
import time
def main():
    print("===== Rock Paper Scissors =====")
    print("Rules:\n- Rock crushes Scissors \n- Scissors cuts paper \n- Paper covers Rock\n- First to win 3 rounds is the champion! ")
    print("-"*50)


    
    play = True
    while play:
        c = 1
        Youscored = 0
        botscored = 0
        while c != 4:
            time.sleep(1)
            print(f"====== Round {c} =====")
            print(f"Score: Your {Youscored}-{botscored} Computer")
        
            #  choice selection logic by both pc and you 
            print("Make you choice:")
            opt = ['Rock', 'Paper', 'Scissors']
            for i,j in enumerate(opt):
                print(str(i + 1) + '. ' + j)
            try:
                choice = int(input("Enter your choice (1-3):"))
                if choice not in [1,2,3]:
                    print("please select a valid option (1-3): ")
                    continue
            except ValueError:
                print("please enter a number")
                continue
            print(f"you chose: {opt[choice -1]}")                
            
            time.sleep(1)
            print("computer is choosing...")
            time.sleep(1)
            comp_choice = random.choice(opt)
            print(f"Computer chose: {comp_choice}")
        
        
            # win logic
            # rock paper sc
            if (choice == 1 and comp_choice == 'paper') or (choice == 2 and comp_choice == 'Scissors') or (choice == 3 and comp_choice == 'Rock'):
                print("You win this round")
                Youscored += 1
                
            elif (choice == 1 and comp_choice == 'Scissors') or (choice == 2 and comp_choice == 'paper') or (choice == 3 and comp_choice == 'Rock'):
                print("computer wins this round")
                botscored += 1
            else:
                print("It's a tie")
                botscored += 0
                Youscored += 0
            c += 1 
        
        
        print(f"\nFinal Score: You {Youscored} - {botscored} Computer")
        if Youscored > botscored:
            print("You are the champion!")
        elif Youscored < botscored:
            print("Computer wins this time.")
        else:
            print("It's a draw overall!")

        play_again = input("\nDo you wish to play again? (Y/N): ")
        if play_again.lower().startswith('n'):
            print("Thank you for playing this game!")
            play = False
    

if __name__ == "__main__":
    main()
