import json
from prime_functions import add,update,mark

if __name__ == "__main__":
    empty_flag=0
    total_tasks = 0
    tasks_data ={} 
    #This checks if taks.json is empty and initialises the index of the last tasks
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        first_char=read_file.read(1)
        if not first_char:
            empty_flag=1
    
    if empty_flag == 0:
        with open("tasks.json", mode="r", encoding="utf-8") as read_file:
                tasks_data = json.load(read_file)
                total_tasks = len(tasks_data)
    print(f"total tasks saved: {total_tasks}")

    while True:
        f_input = input("cli task ")
        if f_input == "exit":
             break
        else:
             
            command , parameters = f_input.split(" ",1)

            if command == "exit":
                break
            elif command == "add":
                add(parameters,total_tasks)
                total_tasks = total_tasks + 1
            elif command == "update":
                update(parameters,total_tasks)
            elif command == "mark":
                mark(parameters,total_tasks)
            '''elif command == "delete":
                delete(parameters)
            elif command =="view":
                view(parameters)'''
        

    print("Bye Bye")