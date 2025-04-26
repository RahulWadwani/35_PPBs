master_ls = []

def add_task():
    add_tasks = str(input("Enter task title: ")).title()
    if add_tasks.title() not in master_ls:
        master_ls.append(f"[] {add_tasks}")
        print(f"Task '{add_tasks}' added successfully!\n")
    else:
        print("Already present in the task.\n")

def show_task():
    print("==== My Tasks====")
    for i,j in enumerate(master_ls):
        print(f"{i+1}. {j}")
    print("="*20 +'\n')
    
def completed_task():
    show_task()
    user = int(input("Enter task number to mark as completed: "))
    for i, j in enumerate(master_ls):
        if user-1 == i:
            val = master_ls[i][3:].strip()
            print(f"Task '{val}' marked as completed.\n")
            master_ls[i] = f"[✓] {j[3:].strip()}"
            break 

def delete_task():
    show_task()
    useri = int(input("Enter task number to be deleted: "))
    for i, j in enumerate(master_ls):
        if useri-1 == i:
            print(f"{master_ls[i][3:].strip()} is deleted from your task.")
            master_ls.pop(i)
            break    

def main():
    flag = True 
    while flag:
        print("==== Task Manager ====")
        print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n0. Exit")
        print("="*20)
        choice = int(input("Enter your choice (0-4): "))
        match choice:
            case 0:
                print('Exited')
            case 1:
                add_task()
            case 2:
                show_task()
            case 3:
                completed_task()
            case 4:
                delete_task()
            case Default:
                print("option does not exists")
        if choice == 0:
            flag == False
            break
                
    
if __name__ == "__main__":
    main()
