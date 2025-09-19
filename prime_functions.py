import json
import datetime
#param here has only the descrition of the task that will be added
def add(param,total_tasks):
    param=param[1:len(param)-1]
    print(param)
    date = str(datetime.datetime.now())
    task = {"id":str(total_tasks + 1),
                   "description":param,
                   "status":"To do",
                   "created":date,
                   "updated":date}

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    #print(type(edit_json))
    edit_json.update({str(total_tasks):task})
    #print(edit_json)
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file)

#param here has the number of the task and then the new descrirtion that will replace the old
def update(param,total_tasks):
    update_index, update_description = param.split(" ",1)
    update_index = int(update_index)
    update_description = update_description[1:len(update_description) - 1]

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    
    edit_json[str(update_index-1)]["description"] = str(update_description)
    edit_json[str(update_index-1)]["updated"] = str(datetime.datetime.now())
    
    
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file)


def mark(param,total_tasks):
    mark_status, mark_index = param.split(" ",1)
    mark_index = int(mark_index)

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    
    edit_json[str(mark_index-1)]["status"] = str(mark_status)
    edit_json[str(mark_index-1)]["updated"] = str(datetime.datetime.now())
    
    
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file)





'''def delete(param, total_tasks):
    delete_index = int(param)
    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
         edit_json = json.load(write_file)
    edit_json[str(delete_index-1)].clear()
    for x in range (delete_index, total_tasks):
        edit

    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file)
'''