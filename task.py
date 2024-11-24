tasks={}

def add_tasks():
    task_name = input("enter task name: ")
    task_priority=input("enter task priority high/medium/low: ")
    tasks[task_name] = task_priority
    print(f'task {task_name} added with priority {task_priority}')
    
def view_tasks():
    if not tasks:
        print('no tasks')
        
    else:
        print('current tasks')
        for task, priority in tasks.items():
            print(f"- {task} (priority:{priority})")
            
            
def remove_task():
    if not tasks:
        print("no tasks")
        return
    tasks_to_remove= input("enter the task name for the remove")    
    if tasks_to_remove in tasks:
        del tasks[tasks_to_remove]
        print(f'Task {tasks_to_remove} removed')         
while True:       
    print("choise")
    print("1/add tasks ")
    print('2/view task')
    print('3/remov')
    print('4/exit')

    choice=input("choice: ")
    if choice == "1":
        add_tasks()
        
    elif choice == "2":
        view_tasks()
        
    elif choice == "3":
        remove_task()
        
    elif choice == '4':
        print('Exiting')
        break
    else:
        print("try again")

