import json
def add(param):
    param=param[0:len(param)]
    print(param)
    jasontasks = [{"id":"1",
                   "desription":"Buy ciggies",
                   "status":"To do",
                   "created":"exampledate",
                   "updated":"exde"},
                   {"id":"2",
                   "desription":"Buy Milk",
                   "status":"Done",
                   "created":"exampledate2",
                   "updated":"exde2"}
                   ]
    x = json.dumps(jasontasks)
    print(x)
x = input("cli tast")
add(x)