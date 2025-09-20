import json
from prime_functions import add,update,mark,delete
from validation import validate_index,validate_mark
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
                total_tasks = len(tasks_data["tasks_list"])
    print(f"total tasks saved: {total_tasks}")

    while True:
        f_input = input("cli task ")
        if f_input == "exit":
             break
        else:




            try:
                command , parameters = f_input.split(" ",1)
            except ValueError:
                 print("Invalid command")
                 continue
            
            if command == "add":
                add(parameters,total_tasks)
                total_tasks = total_tasks + 1
            elif command == "update":

                update_index, update_description = parameters.split(" ",1)
                update_description = update_description[1:len(update_description) - 1]

                if validate_index(update_index,total_tasks) == 1:
                     continue
                
                update_index = int(update_index)

                update(update_index,update_description)
            elif command == "mark":
                mark_status, mark_index = parameters.split(" ",1)
                if validate_mark(mark_status)== 1:
                     continue
                    
                if validate_index(mark_index,total_tasks) == 1:
                     continue
                
                mark_index = int(mark_index)

                mark(mark_index,mark_status)
            elif command == "delete":
                
                if validate_index(parameters,total_tasks) == 1:
                     continue
                
                delete(parameters,total_tasks)
                total_tasks = total_tasks - 1
            else:
                 print("Invalid command")
                 continue
            
            '''elif command == "view":
                view()'''
        

    print("Bye Bye")