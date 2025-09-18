import json
import datetime
def add(param,total_tasks):

    param=param[0:len(param)]
    date = str(datetime.datetime.now())
    task = {"id":str(total_tasks + 1),
                   "desription":param,
                   "status":"To do",
                   "created":date,
                   "updated":date}

    with open ("tasks.json",mode="r",encoding="utf-8") as write_file:
        edit_json = json.load(write_file)
    #print(type(edit_json))
    edit_json.update({str(total_tasks + 1):task})
    #print(edit_json)
    with open ("tasks.json",mode="w",encoding="utf-8") as write_file:
        json.dump(edit_json,write_file)
