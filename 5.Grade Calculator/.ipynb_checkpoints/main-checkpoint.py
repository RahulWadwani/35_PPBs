def check_grades(avg):
    if avg >= 90:
        return 'A'
    elif ((avg < 90) and (avg >= 80)):
        return 'B'
    elif ((avg < 80) and (avg >= 70)):
        return 'C'
    elif ((avg < 70) and (avg >= 60)):
        return 'D'
    elif ((avg < 60) and (avg >= 50)):
        return 'E'
    else:
        return 'Fail'
        
def main():
    int_score = 0
    int_val = 0 
    
    while True:
        score = input("Enter a test score (or 'done'): ")
        if score.lower() == 'done':
            break
        int_score += int(score)
        int_val += 1
        avg = round(int_score/int_val,2)
        print(f"Average score:{avg}")
        print(check_grades(avg))
    

if __name__ == "__main__":
    main()
