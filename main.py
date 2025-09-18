import datetime
import json


if __name__ == "__main__":
    
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        first_char=read_file.read(1)
        if not first_char:
            total_tasks= 0
        else:
            tasks_data = json.load(read_file)
            total_tasks = len(tasks_data)
    print(total_tasks)
    '''while True:
        x = datetime.datetime.now()
        command , parameters = input("").split(" ",1)

        if command == "exit":
            break
        elif command == "add":
            add(parameters)
        elif command == "update":
            update(parameters)
        elif command == "mark":
            mark(parameters)
        elif command == "delete":
            delete(parameters)
        elif command =="view":
            view(parameters)
    '''

    print("Bye Bye")