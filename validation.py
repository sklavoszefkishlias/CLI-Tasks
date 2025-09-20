def validate_index(index,total_tasks):
    try:
        if int(index) < 1 or int(index) > total_tasks:
            print("Invalid task index")
            return 1
    except ValueError:
            print("Floats cant be indexes")
            return 1
    return 0 

def validate_mark(mark):
     if mark == "To-do" or mark == "In-progress" or mark == "Done":
          return 0
     else:
          print("Invalid marking")
          return 1