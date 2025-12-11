tasks = []
while True:
    job = input("Add, show, or remove task?")
    if job == "add":
        task = input("Enter task to add: ")
        tasks.append(task)
        print(f'Task "{task}" added.') 
    elif job == "show":
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif job == "remove":
        task_num = input("Enter task number to remove: ")
        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        else:
            print("Invalid task number.")