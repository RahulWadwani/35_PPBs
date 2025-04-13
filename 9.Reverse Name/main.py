def main():
    print("Reverse Name Generator")
    while True:
        name = input("Enter a name: ")
        reverse_name = name[::-1]
        print(f"Your reversed name is:{reverse_name}")
        print(f"In a parallel universe, they call you {reverse_name}")
        query = input("Try another name? (y/n): ")
        if query == 'n':
            break
        

if __name__ == "__main__":
    main()
