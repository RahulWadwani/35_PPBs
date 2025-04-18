def main(first,second):
    print("Color Mixer")
    colors = {
        ("red","blue"):"purple",
        ("red","yellow"):"orange",
        ("blue","yellow"):"green",
        ("blue","green"):"teal",
        ("red","white"):"pink",
        ("red","green"):"brown",
    }
    
    while True:
        if first.lower() == colors[0]
        print(f"when you mix {first} and {second}, you get !")
        mcolor = input("Mix more colors? (y/n): ")
        if mcolor == 'n':
            break
if __name__ == "__main__":
    fcolor = input("Enter first color: ")
    scolor = input("Enter second color: ")
    main(fcolor,scolor)
