import time,random 

def points_cal(res):                # points calculator function
    if res < 5:
        return 5 - round(res)
    else:
        return 1

def get_word(dct):                 # getting the word from the dictionary
    keys = list(dct.keys())
    return random.choice(keys)

def main():
    word_pairs = {
        'sky'   : ['cloud', 'bird', 'blue', 'fly', 'sun'],
        'water' : ['drink', 'ocean', 'swim', 'fish', 'boat'],
        'food'  : ['eat', 'cook', 'tasty', 'meal', 'restaurant'],
        'music' : ['song', 'feel', 'dance', 'listen', 'band', 'rhythm'],
        'book'  : ['read', 'story', 'page', 'author', 'library'],
        'tree'  : ['leaf', 'green', 'forest', 'wood', 'shade'],
        'car'   : ['drive', 'road', 'wheel', 'travel', 'speed'],
        'dog'   : ['pet', 'bark', 'walk', 'loyal', 'puppy']
    }
    score, tot = 0, 5
    while True:
        print("=== Word Association Game ===")
        print("Respond with a related word quickly! ")   
        print(f"Prompt word: {get_word(word_pairs)}")
        # capturing the response time 
        init = time.time()
        res = input("Quick! Type a word related to this prompt! \n>")
        response_time = time.time() - init
        
        # pointing system 
        print(f"Good Association! : +{points_cal(response_time)} points (answered in {round(response_time,1)}s)")
        score += points_cal(response_time)
        print(f"Score: {score}/{tot} possible points")
        tot += 5
        prompt_word = random.choice(list(word_pairs.keys()))
        ask = input("Play again? (yes/no)")
        if ask == 'n' or ask == 'no':
            print(f"Final score : {score}.\nThanks for playing")
            break

if __name__ == "__main__":
    main()
