def main(goal, steps):
    if goal > steps:
        print(f"you need {goal - steps} more steps to reach your goal!")
    elif goal == steps:
        print(f"you have achieved your goal for today")
    else:
        print(f"Congratulations! you've exceeded your goal by {steps - goal} steps")

if __name__ == "__main__":
    dsg = int(input("Enter you daily step goals: "))
    st = int(input("How many steps have you taken: "))
    main(dsg,st)
