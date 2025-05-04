def getText():
    print("Enter or paste your text below (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    full_text = "\n".join(lines)
    word_analyzer(full_text)

def word_analyzer(line):
    if "." in line:
        sents = line.split(".")
    else:
        sents = line.split("?")
    sent = len(sents) - 1
    word = 0
    for i in range(sent):
        word += len(sents[i].strip().split(" "))
    ch = len(line)
    ch_ = len(line.replace(" ", ""))
    
    avg_ws = round(word / sent, 1) if sent != 0 else 0
    t = round(ch / word, 1) if word != 0 else 0

    print("==== Text Analysis Results =====")
    print(f"Words                         : {word}")
    print(f"Characters (with spaces)      : {ch}")
    print(f"Characters (without spaces)   : {ch_}")
    print(f"Sentences                     : {sent}")
    print(f"Average words per sentence    : {avg_ws}")
    print(f"Average characters per word   : {t}")

def main():
    while True:
        print("\n==== Word Counter ====")
        print("Choose an option:\n1. Enter text to analyze.\n2. Exit")
        try:
            choice = int(input("Your choice (1-2): "))
            match choice:
                case 1:
                    getText()
                case 2:
                    print("Exiting. Goodbye!")
                    break
                case _:
                    print("Select either 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
