import random

def main():
    print("Music Recommender")
    genre = {'rock':['Indian Ocean', 'parikrama', 'Indus Creed'],
             'hip-hop':['Divine','Raftar','Humankind'],
             'pop':['Arijit Singh','Shreya Ghoshal','A.R. Rehman']}
    music = input("What genre do you like? (rock/hip-hop/pop): ")
    if music.lower() not in genre:
        print("Sorry, I don't know that genre.")
    else:
        print(f"check out {random.choice(genre[music])}")

if __name__ == "__main__":
    main()
