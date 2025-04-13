import random 

def main():
    print("===== Coin Flip Game =====")
    coin = ['heads', 'tails']
    while True:
        guess = input("Enter your guess (heads/tails):")
        
        # random choice heads or tails using the inbuilt python functions 
        coin_chose = random.choice(coin)
        print(f'The coin shows: {coin_chose}')

        # if guess is correct you win else try again
        if guess.strip().lower() == coin_chose.strip().lower():
            print("You guessed correctly! you win")
        else:
            print("Sorry, wrong guess. Try again!")

        # play again logic
        revert = input('Play again? (yes/no):')
        if revert == 'no' or revert == 'n':
            break


if __name__ == "__main__":
    main()
