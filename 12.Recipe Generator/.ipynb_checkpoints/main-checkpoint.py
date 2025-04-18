import random

def main():
    dct ={
        'proteins':['Eggs','Chicken','Fish','pork','milk'],
        'veggies':['Spinach','broccoli','sprouts','green peas','asparagus'],
        'flavor':['garlic, olive oil and lemon juice','cheese','butter, black pepper and chaat masala'],
        'carb':['brown rice','oats','quinoa','barley','millets','sweet potato'],
        'methods':['stir fry','boiling','steaming','roasting','grilling','pressure cooking']
         }

    # output: {flavor} {method} {protein} with {veggies} and {carb}
    while True:
        f, m, p, v, c = random.choice(dct['flavor']),random.choice(dct['methods']), random.choice(dct['proteins']),random.choice(dct['veggies']),random.choice(dct['carb'])
        
        print(f"Your random recipe: {f} {m} {p} with {v} and {c}")
        regenerate = input("Generate another recipe? (y/n): ")
        if regenerate.lower() == 'n':
            break
    

if __name__ == "__main__":
    main()
