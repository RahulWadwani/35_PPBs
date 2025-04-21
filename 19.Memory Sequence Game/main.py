import random 
import os
import time 

def clear_screen():
    """clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")
    
def main():
    print("=== Memory Sequence Game ===")
    print("Remember the sequence and type it back!")
    print("Rules:")
    print("- Watch as numbers appear one by one")
    print("- After the sequence is shown, type it back in order")
    print("- Each round adds one more number to remember")
    print("- How far can you go?\n")
    input("Press Enter to start")
    sequence = []
    current_round = 1
    game_over = False 
    while not game_over:
        sequence.append(random.randint(1,9))
        clear_screen()
        print(f"\n ===Round {current_round} ===")
        print(f"remember this sequence {len(sequence)} numbers: ")

        for number in sequence:
            time.sleep(0.5)
            print(f"\n{number}")
            time.sleep(0.5)
            clear_screen()
        print("\nNow repeat the sequence by typing each number, seperated by spaces")
        player_answer = input(">")
        try:
            player_sequence = [int(num) for num in player_answer.split()]
        except ValueError:
            print(" please enter numbers only!")
            game_over = True
            continue
        
        if player_sequence == sequence:
            print(f"Congrats! you rememeberd all {len(sequence)} numbers!")
            current_round += 1
            time.sleep(2)
        else:
            print(f"Game over! you remembered all {current_round -1} numbers")
            print(
                f"the correct sequence was: {"".join(str(num) for num in sequence)}")
            game_over = True
            
        if game_over:
            play_again = input("Do you wish to play again? (yes/no) ").lower()
            if play_again.startswith('y'):
                sequence = []
                current_round = 1
                game_over = False
            else:
                print("Thank for playing")

                
            
    
if __name__ == "__main__":
    main()
