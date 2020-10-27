"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={
    "Jill":{
        "age":26,
        "job":"biologist",
        "relation":{
            "Zalike":"friend",
            "John":"partner"
        }
    },
        "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}
age0=0
for key in group:
    age=group[key]["age"]
    if age > age0:
        name=key
    age0=age

    
rel=0
name_number=0
for name,people in group.items():
    rel+=len(people["relations"])
    name_number+=1
    average_rel=rel/name_number

    
age0=0
for name,people in group.items():
    age=people["age"]
    if age > age0 and len(people["relations"])>=1:
        name=name
    age0=age 

    
age0=0
for name,people in group.items():
    age=people["age"]
    for r in people["relations"].values():
        nu=0
        if r=="friend":
            nu=nu+1
        if age > age0 and nu >= 1:
            nam=name
    age0=age 
