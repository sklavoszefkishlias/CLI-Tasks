def validate_index(index,total_tasks):
    #Exception is for entering floats
    #If statment are for valid int indexes
    try:
        if int(index) < 1 or int(index) > total_tasks:
            print("Invalid task index")
            return 1
    except ValueError:
            print("Floats cant be indexes")
            return 1
    return 0 

def validate_mark(mark):
     if mark.lower() == "to-do":
          return "To-do"
     elif mark.lower() == "in-progress":
          return "In-progress"
     elif mark.lower() == "done":
          return "Done"
     else:
          print("Invalid marking")
          return "Invalid"