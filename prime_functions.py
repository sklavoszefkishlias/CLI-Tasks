import json
import datetime
#param here has only the descrition of the task that will be added
def add(param,total_tasks):
    param=param[1:len(param)-1]
    date = str(datetime.datetime.now())
    task = {"id":str(total_tasks + 1),
                   "description":param,
                   "status":"To-do",
                   "created":date,
                   "updated":date}

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    edit_json["tasks_list"].append(task)
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
    #Correction of "id" propperties
    for x in range (delete_index-1, total_tasks-1):
        edit_json["tasks_list"][x]["id"] = str(int(edit_json["tasks_list"][x]["id"])-1) 

    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file,indent=4)


def view(param):
    if param == "None":
        with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
            edit_json = json.load(write_file)
        for x in edit_json["tasks_list"]:
            print(f"{x["id"]}. {x["description"]} >{x["status"]}")

    elif param.lower() == "done":
        with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
            edit_json = json.load(write_file)
        y=1
        for x in edit_json["tasks_list"]:
            if x["status"]=="Done":
                print(f"{y}. {x["description"]} >{x["status"]}")
                y = y + 1


        
    elif param.lower() == "to-do":
        with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
            edit_json = json.load(write_file)
        y=1
        for x in edit_json["tasks_list"]:
            if x["status"]=="To-do":
                print(f"{y}. {x["description"]} >{x["status"]}")
                y = y + 1


    elif param.lower() == "in-progress":
        with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
            edit_json = json.load(write_file)
        y=1
        for x in edit_json["tasks_list"]:
            if x["status"]=="In-progress":
                print(f"{y}. {x["description"]} >{x["status"]}")
                y = y + 1

