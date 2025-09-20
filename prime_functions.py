import json
import datetime
#param here has only the descrition of the task that will be added
def add(param,total_tasks):
    param=param[1:len(param)-1]
    print(param)
    date = str(datetime.datetime.now())
    task = {"id":str(total_tasks + 1),
                   "description":param,
                   "status":"To-do",
                   "created":date,
                   "updated":date}

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    #print(type(edit_json))
    edit_json["tasks_list"].append(task)
    #print(edit_json)
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file,indent=4)

#param here has the number of the task and then the new descrirtion that will replace the old
def update(update_index,update_description):

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    
    edit_json["tasks_list"][update_index-1]["description"] = str(update_description)
    edit_json["tasks_list"][update_index-1]["updated"] = str(datetime.datetime.now())
    
    
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file,indent= 4)


def mark(mark_index,mark_status):

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    
    edit_json["tasks_list"][mark_index-1]["status"] = str(mark_status)
    edit_json["tasks_list"][mark_index-1]["updated"] = str(datetime.datetime.now())
    
    
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file,indent=4)





def delete(param, total_tasks):
    delete_index = int(param)
    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
         edit_json = json.load(write_file)
    edit_json["tasks_list"].pop(delete_index-1)
    for x in range (delete_index-1, total_tasks-1):
        edit_json["tasks_list"][x]["id"] = str(int(edit_json["tasks_list"][x]["id"])-1) 

    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file,indent=4)

'''
def view(param):
    if param == "done":
        
    elif param == "to-do"

    elif param == "in-progress"
'''